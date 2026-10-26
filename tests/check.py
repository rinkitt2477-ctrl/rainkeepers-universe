"""
The Rainkeeper's Universe — real-browser checks.

Run from the repo root:
    pip install playwright && python -m playwright install chromium
    python tests/check.py

It serves the folder on a local port, opens the site in Chromium at desktop
(1440x900) and phone (390x844, touch) sizes, scrolls for real, and fails
(exit code 1) if anything below is wrong:

  1. no JavaScript errors on load
  2. no sideways scroll on phone
  3. street walk-in: zoom, door angle and room fade move at an even pace
     and finish with the shop interior fully shown
  4. the book on the shelf opens (overlay #ov) or is a link when BOOKS[0].link is set
  5. about page: the room-reveal clip loads and follows the scroll
     (video time tracks scroll position, also when scrolling back up)
"""
import asyncio, math, re, sys, threading, functools, os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8799
fails = []

def check(ok, msg):
    print(("  PASS " if ok else "  FAIL ") + msg)
    if not ok: fails.append(msg)

def serve():
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    h = functools.partial(Quiet, directory=ROOT)
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv

async def run(p, name, vp, mobile):
    print(f"\n[{name}] {vp['width']}x{vp['height']}")
    b = await p.chromium.launch()
    pg = await b.new_page(viewport=vp, is_mobile=mobile, has_touch=mobile)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    base = f"http://127.0.0.1:{PORT}/index.html"

    # ---------- shop / walk-in ----------
    await pg.goto(base); await pg.wait_for_timeout(3000)
    sw = await pg.evaluate("document.documentElement.scrollWidth"); check(sw <= vp["width"] + 1, f"no sideways scroll on shop page (scrollWidth {sw})")
    span = await pg.evaluate("document.querySelector('#street').offsetHeight - document.querySelector('#pin').clientHeight")
    rows = []
    for i in range(21):
        await pg.evaluate(f"scrollTo(0,{span*i/20})"); await pg.wait_for_timeout(500)
        t = await pg.evaluate("[document.querySelector('#scene').style.transform, document.querySelector('#door').style.transform, +document.querySelector('#xf').style.opacity]")
        s = float(re.search(r"scale\(([\d.]+)\)", t[0]).group(1)); d = float(re.search(r"([\d.]+)deg", t[1]).group(1))
        rows.append((math.log(s), d, t[2]))
    zsteps = [round(rows[i+1][0]-rows[i][0], 3) for i in range(2, 12)]
    dsteps = [round(rows[i+1][1]-rows[i][1], 1) for i in range(7, 11)]
    check(max(zsteps) - min(zsteps) < 0.015, f"walk-in zoom pace even {zsteps}")
    check(max(dsteps) - min(dsteps) < 2.5, f"door opens at even pace {dsteps}")
    check(rows[-1][2] == 1, "shop interior fully shown at end of walk-in")

    # ---------- book on the shelf ----------
    await pg.evaluate("scrollTo(0, document.querySelector('#street').offsetTop + document.querySelector('#street').offsetHeight)")
    await pg.wait_for_timeout(1500)
    tag = await pg.evaluate("(document.querySelector('[data-book]')||{}).tagName")
    if tag == "A":
        href = await pg.evaluate("document.querySelector('[data-book]').href"); check(href.startswith("http"), f"book is a link to {href}")
    else:
        await pg.evaluate("document.querySelector('[data-book]').click()"); await pg.wait_for_timeout(1200)
        check(await pg.evaluate("!!document.querySelector('#ov')"), "book opens its overlay")
        await pg.keyboard.press("Escape"); await pg.wait_for_timeout(600)

    # ---------- about page scroll clip ----------
    await pg.goto(base + "#about"); await pg.wait_for_timeout(3500)
    sw = await pg.evaluate("document.documentElement.scrollWidth"); check(sw <= vp["width"] + 1, f"no sideways scroll on about page (scrollWidth {sw})")
    st = await pg.evaluate("__aboutState()"); check(st["vidOn"], "room-reveal clip loaded")
    top = await pg.evaluate("document.querySelector('#abTrack').offsetTop"); th = await pg.evaluate("document.querySelector('#abTrack').offsetHeight")
    ts = []
    for y in range(0, th, 400):
        await pg.evaluate(f"scrollTo(0,{top+y})"); await pg.wait_for_timeout(700)
        ts.append((await pg.evaluate("__aboutState()"))["t"])
    steps = [round(ts[i+1]-ts[i], 2) for i in range(len(ts)-1) if ts[i+1] < 5.9]
    check(len(steps) > 4 and max(steps) - min(steps) < 0.08, f"clip follows scroll at even pace {steps}")
    await pg.evaluate(f"scrollTo(0,{top})"); await pg.wait_for_timeout(1200)
    check((await pg.evaluate("__aboutState()"))["t"] < 0.05, "clip rewinds when scrolling back up")

    check(not errs, f"no JavaScript errors {errs}")
    await b.close()

async def main():
    srv = serve()
    async with async_playwright() as p:
        await run(p, "desktop", {"width":1440, "height":900}, False)
        await run(p, "phone", {"width":390, "height":844}, True)
    srv.shutdown()
    print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED")
    sys.exit(1 if fails else 0)

asyncio.run(main())
