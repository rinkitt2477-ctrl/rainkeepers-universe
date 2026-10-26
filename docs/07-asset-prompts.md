# 07 · Prompt สำหรับสร้างภาพและวิดีโอ

เจ้าของสร้างภาพ/วิดีโอเองด้วยเครื่องมือ AI (เช่น ChatGPT) แล้วส่งไฟล์มา งานของ AI ฝั่งโค้ดคือเขียน prompt ให้ + encode + วางในเว็บ
ทุกครั้งให้แนบภาพต้นฉบับที่เกี่ยวข้องไปด้วย เพื่อให้ห้อง/ร้านหน้าตาเดิม

brief ชุดแรก (วิดีโอหน้าร้าน, ภาพในร้าน) อยู่ใน `docs/asset-brief-phase-b.md`

## วิดีโอ room-reveal (ที่ใช้อยู่ตอนนี้)
แนบ `img/shop-interior.jpg`
```
Image-to-video. Use the attached image as the room — keep everything identical
(the empty dark-wood bookcase in the centre, brass lantern with a lit candle,
black cat on the rainy window sill at left, warm table lamps, library ladder at right).

One continuous camera move, no cuts, 6 seconds, 16:9, 1920x1080, 24 fps, no audio.
0–3.5 s: start in a tight close-up on the middle shelf of the empty bookcase
(lantern visible, bookcase centred), then dolly straight backwards along the
centre line until the whole room is visible exactly as in the reference image.
Smooth, slow, constant speed, no rotation, no handheld shake.
3.5–6 s: camera keeps drifting back very slightly while soft warm mist / rain haze
rolls in from the left and right edges and thickens until the last frame is
almost entirely a flat warm parchment beige (#d2b88e).
Rain keeps running down the window; candle and lamps flicker gently.
No people, no text, no logos, no new objects.
```

## วิดีโอ room-reveal แนวตั้งสำหรับมือถือ (roadmap ข้อ 6)
แนบ `img/shop-interior.jpg`
```
Image-to-video, vertical 9:16, 1080x1920, 24 fps, 6 seconds, no audio, no cuts.
Same room as the attached image, everything identical (empty dark-wood bookcase,
brass candle lantern, black cat on the rainy window sill, warm lamps, ladder).
0–3.5 s: start in a tight close-up on the middle shelf of the bookcase (lantern visible,
bookcase centred), then dolly straight backwards along the centre line, constant speed,
until the bookcase and as much of the room as fits a vertical frame are visible —
show the rainy window with the black cat at the left edge if possible.
3.5–6 s: warm mist rolls in from the left and right edges until the last frame is
almost entirely flat warm parchment beige (#d2b98f).
No rotation, no shake, no people, no text, no new objects.
```
encode แบบเดียวกับ 06 (เปลี่ยน scale เป็น 720:1280 สำหรับไฟล์เล็ก) แล้วใน `About` เลือกไฟล์ด้วย `innerWidth < innerHeight`

## ภาพแชร์ลิงก์ (Open Graph) 1200×630 (roadmap ข้อ 8)
ทำจาก `img/street.jpg` ได้ด้วยโค้ด (crop กลางภาพ + ตัวหนังสือ "The Rainkeeper's Universe" ฟอนต์ Prompt สีทอง) ไม่ต้องใช้ AI

## กฎของภาพ/วิดีโอทุกชิ้น
- ไม่มีคน ไม่มีตัวหนังสือที่อ่านได้ ไม่มีโลโก้/แบรนด์จริง ไม่มีลายน้ำ
- โทนเดิม: กลางคืน ฝน แสงส้มทองอุ่น แมวดำตัวเดิม
- วิดีโอที่วางทับภาพนิ่ง ต้องกล้องนิ่งและองค์ประกอบตรงภาพนิ่ง
