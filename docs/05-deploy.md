# 05 · การขึ้นเว็บ

## ตอนนี้: GitHub Pages

- Repository: `rinkitt2477-ctrl/rainkeepers-universe` (Public), branch `main`
- เว็บ: **https://rinkitt2477-ctrl.github.io/rainkeepers-universe/**
- ตั้งค่า: Settings → Pages → Source "Deploy from a branch" → `main` / `(root)`
- `.nojekyll` อยู่ที่ root เพื่อให้ GitHub เสิร์ฟไฟล์ตรง ๆ ไม่ผ่าน Jekyll
- อัปเดต: push ขึ้น `main` → GitHub สร้างเว็บใหม่เองใน 1–3 นาที (ดูที่แท็บ Actions → "pages build and deployment")
- ข้อจำกัด GitHub Pages: ไซต์ ≤ 1 GB, bandwidth soft limit 100 GB/เดือน, ไฟล์เดี่ยวใน git ไม่ควรเกิน 100 MB, บัญชีฟรีต้อง repo Public, ห้ามใช้เป็นโฮสต์เชิงพาณิชย์ — https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

### ขั้นตอนอัปเดตมาตรฐาน

```bash
python tests/check.py                       # ต้อง ALL PASS ก่อน
git add -A
git -c user.name="ผู้เก็บเสียงฝน" -c user.email="rainkeeper@users.noreply.github.com" \
    commit -m "อธิบายสั้น ๆ ว่าเปลี่ยนอะไร"
git push origin main
```
แล้วเปิดลิงก์เว็บจริง (Ctrl+F5) เช็กอีกรอบ ถ้า path ไฟล์ผิดตัวพิมพ์เล็ก/ใหญ่ บน GitHub Pages จะ 404 ทั้งที่ในเครื่องใช้ได้

## ทางเลือก: repo Private + Cloudflare Pages (เสนอเจ้าของไว้ ยังไม่ทำ)

ใช้เมื่อเจ้าของไม่อยากให้คนใน GitHub เห็นไฟล์/ประวัติ
1. GitHub: Settings → General → Danger Zone → Change visibility → Private (GitHub Pages จะหยุดทำงาน)
2. Cloudflare: สมัครฟรี → Workers & Pages → Create → Pages → Connect to Git → เลือก repo นี้
3. Build command: ว่าง · Build output directory: `/` (เว็บเป็นไฟล์ static ล้วน)
4. ได้ลิงก์ `<project>.pages.dev` → ทุก push ขึ้น `main` deploy อัตโนมัติ
5. ยังต้องยืนยันตอนเชื่อมว่า Cloudflare มองเห็น repo Private (คู่มือไม่ได้ระบุชัด) — https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/
6. ข้อควรรู้: เว็บยังเปิดได้ทุกคนที่มีลิงก์ (ไม่มีทางฟรีที่ทำให้เว็บต้องล็อกอิน)

## สำเนาใน Claude (artifact)

เจ้าของมีหน้าเว็บเดียวกันเป็น artifact ส่วนตัวใน claude.ai (ต้องล็อกอิน Claude ถึงเปิดได้) ใช้ดูตัวอย่างระหว่างทำ ถ้าแก้ใน repo แล้วอยากให้ artifact ตรงกัน ต้องให้ Claude publish ใหม่ — artifact มี CSP ที่อนุญาตแค่ Google Fonts จึงต้องคงกฎ "ไม่โหลดจากโดเมนภายนอก"

## Netlify Drop (ทางเลือกสำรอง)

ลากโฟลเดอร์ไปวางที่ https://app.netlify.com/drop (ต้องล็อกอินเพื่อไม่ให้ติดรหัสผ่านชั่วคราว) แนะนำไฟล์เดี่ยว < 10 MB รวม < 50 MB — https://docs.netlify.com/start/quickstarts/netlify-drop-quickstart/
