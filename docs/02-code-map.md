# 02 · แผนที่โค้ด (`index.html`)

ไฟล์เดียว ลำดับคือ `<head>` (meta, fonts, `<style>`) → markup → `<script>` ค้นหาด้วยหัวคอมเมนต์ `/* ---------- ... */`

## CSS (ในบล็อก `<style>`)

| หัวคอมเมนต์ | คุมอะไร |
|---|---|
| `nav` | แถบเมนูบน, ปุ่มเสียง, slider |
| `street (photo scene)` | `.street` (400vh), `.pin` (sticky 100svh), `.scene`, `.doorway` (left 62.68% top 32.73% w 9.99% h 42.72% ของภาพถนน), `.door` (บานพับขวา), `.opensign` |
| `interior (photo bookcase)` | `#xf` ห้องในร้าน, `#stageWrap/#stage`, `.bcbox` (กรอบตู้ left 28.921% width 42.158% ของภาพในร้าน), `.pbook`, `.tip` การ์ดเรื่องย่อ |
| `phase A: ...` | preloader, entrance, cursor, chapter cards |
| `open book` / `reader` | overlay เปิดเล่ม (`#ov`, `.tome`) และหน้าอ่าน (`#reader`) |
| `rooms` | `.room` พื้นฐานของหน้า journal |
| `about: the rain letter, scroll scene` | `#v-about`, `.ab-track`, `.ab-scene` (sticky), `.ab-cam`, `.ab-mist`, `.ab-intro`, `.ab-papers`, `.paper` `.letter` `.gnote`, `.ab-letter.ab-end` |
| `journal` | `.pane` กระจก, `#fog` |

**ระวังชื่อคลาสชนกัน** (เคยพังมาแล้ว): `.pin` = ฉาก sticky หน้าร้าน ส่วนหมุดปักกระดาษคือ `.pushpin` · `.note` = ข้อความเล็กหน้าร้าน ส่วนโน้ตกระดาษคือ `.gnote`

## JavaScript (ตามลำดับในไฟล์)

| ส่วน | ทำอะไร | ตัวเลข/จุดสำคัญ |
|---|---|---|
| `/* ===== แก้ไขเนื้อหาตรงนี้ ===== */` | `AUTHOR`, `BOOKS`, `ENTRIES`, `SHOP_OPENED` | ดู docs/03 |
| ค่าคงที่ | `REDUCE = false`, `CALM = false` | **ห้ามเปลี่ยนเป็น true** |
| `store` | localStorage แบบ try/catch | keys: `rainVol`, `fontSize`, `lastRead` |
| `Sound` | WebAudio สร้างเสียงฝน | bed: pink noise → highpass 900 (gain .38) + bandpass 3800 (.32), brown → lowpass 300 (.12) · หยดน้ำ 8 ครั้ง/50ms (ในร้าน 5) prob .7 · ฟ้าร้องสุ่มทุก 60–120 วิ (peak ใกล้ .9 ไกล .5) · lowpass ข้างนอก 11000 / ในร้าน 2600 · `level() = .6 * (vol/100)^2` · ค่าเริ่ม 45 · `Sound.bell()` กระดิ่งประตู |
| `Street` | ฝน canvas 3 ชั้นบนถนน + กระเซ็น | |
| `Glass` | หยดน้ำบนกระจก | |
| `liveLoop(video, scene)` | เล่นวิดีโอลูปเมื่ออยู่ในจอ, ลองเล่นใหม่เมื่อผู้ใช้แตะ/เลื่อน, เพิ่มคลาส `has-live` | ใช้กับ `#streetVid`, `#shopVid` |
| `Walk` | เดินเข้าร้านตามการเลื่อน | `progress()` = ระยะเลื่อนใน `.street` · `tick()` ตามเป้าแบบ `sp += d * .22` · **ซูม** `S = SMAX ^ seg(p,.03,.62)` (เรขาคณิต = ความเร็วคงที่) โดย `SMAX = max(1.4, min(.74*vh/(.4272*H), .62*vw/(.0999*W)))` จุดศูนย์กลางประตู `DX .6767, DY .541` · **ประตู** `rotateY(80 * seg(p,.3,.6))` เชิงเส้น · **ห้อง** opacity `seg(p,.6,.9)` + scale 1.05→1 เชิงเส้น · `enter()` เลื่อนอัตโนมัติ 6 วิ ความเร็วคงที่ (ยกเลิกเมื่อผู้ใช้เลื่อนเอง) |
| `WinRain`, `Dust` | ฝนหน้าต่างในร้าน, ฝุ่นแสง/หิ่งห้อย | แสงฝุ่นอิงพิกัดภาพในร้าน 2576 กว้าง: `L(1102,715,260) L(1159,276,150) L(77,644,300) L(811,528,200) L(1848,528,200) L(2454,489,260)` · `Dust.hover(el)` รวมหิ่งห้อยรอบเล่มที่ชี้ |
| `renderShelves()` | วางหนังสือบนตู้ | เล่มแรกใช้ `PAINTED {x:393,y:200,w:42,h:152}` บนภาพ `IMG {w:1086,h:1448}` (crop สันจาก bookcase.jpg) · เล่มถัดไปใช้ `SLOTS` · ถ้า `b.link` มีค่า → เป็น `<a target=_blank>` ไปหน้านิยาย |
| `openBook`, `openReader` | overlay เล่ม / หน้าอ่าน | Esc ปิดได้ |
| `Fog`, `renderEntries` | หน้า journal | |
| `renderToc` | การ์ดบทใต้ตู้ | ซ่อนถ้าไม่มีบท |
| cursor, preloader | | |
| `About` | หน้า about | ดูด้านล่าง |
| routing | `route()` สลับหน้า, `updateNav()` เมนูทึบเมื่อเลื่อน | `About.show()/hide()`, `Fog.show()/hide()` |

### `About` (สำคัญ — เพิ่งทำ)

- วิดีโอ `#abVid` **ไม่เคย play** ใช้แค่ `currentTime` (scrub)
- โหลดทั้งไฟล์เป็น blob (`fetch → URL.createObjectURL`) เพื่อให้ seek ได้ทุกเฟรมแม้ server ไม่รองรับ Range; ถ้า fetch พังจะใช้ src ตรง
- เลือกไฟล์: กว้าง ≤ 900px หรือ Save-Data → 720p, ไม่งั้น 1080p
- ความยาว track: `lb` = ขอบล่างของกระดาษแผ่นสุดท้าย (`#abLast`), `end = lb / PULL` (`PULL = .6`), ความสูง track = `end + vh`
- `p = clamp((scrollY - track.top) / end)` → **clip progress = p (เชิงเส้น = ความเร็วคงที่)**
  - 0–0.6 (0–3.6 วิ) กล้องถอยจากตู้จนเห็นทั้งห้อง ระหว่างนั้นข้อความลอยผ่าน
  - 0.6–1 (3.6–6 วิ) หมอกกลืนห้องจนเป็นสี `--pp`
- smoothing: `cur += (target - cur) * .22`, set `currentTime` เมื่อไม่ได้ seeking และต่างเกิน 1/60 วิ, seek ซ้ำใน `seeked`
- fallback ก่อนวิดีโอโหลด: ซูมภาพนิ่ง `shop-interior.jpg` (เริ่ม 2.1 บนคอม 1.45 บนมือถือ) + หมอก CSS (`.ab-mist`) → ซ่อนเมื่อ `.vid-on`
- `window.__aboutState()` คืนค่า `{vidOn, t, target, c}` ใช้ในเทสต์
- หน่วย layout: `--u = min(100vh/800, 100vw/716)`; มือถือ/แนวตั้ง `--u = min(100vw/390, 1.6px)` และทุกอย่างเรียงเป็นคอลัมน์เดียวเริ่ม 112vh
- ตำแหน่งบนคอม: หัวข้อ `top: 940/8 vh`, กระดาษ `top: 1500/8 vh` (จดหมายซ้าย โน้ตขวาต่ำลง 38vh)
