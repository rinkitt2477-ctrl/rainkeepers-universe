# The Rainkeeper's Universe — งานช่วง B (ไฟล์ภาพและวิดีโอ)

เอกสารนี้ใช้สั่งงาน AI สร้างภาพหรือวิดีโอ ไฟล์ทุกชิ้นจะเอาไปวางซ้อนบนเว็บที่ทำเสร็จแล้ว จึงต้องทำ **ตามเงื่อนไขทุกข้อ** ไม่อย่างนั้นภาพจะวางไม่ตรงกับปุ่มและวัตถุที่กดได้บนหน้าเว็บ

ต้นฉบับมี 2 รูป แนบไปด้วยทุกครั้งที่สั่งงาน
- `street.jpg` — หน้าร้านหนังสือกลางสายฝน (1672 × 941 px)
- `bookcase.jpg` — ตู้หนังสือไม้โบราณ มีหนังสือ 1 เล่มบนชั้นบนสุด และตะเกียงเทียนบนชั้นที่สาม (1086 × 1448 px)

---

## ชิ้นที่ 1 · วิดีโอหน้าร้าน (สำคัญที่สุด)

**ใช้รูปต้นฉบับ:** `street.jpg` (Image to Video)

**เงื่อนไขที่ต้องผ่านทุกข้อ**
- กล้องอยู่นิ่ง 100% ห้ามซูม ห้ามแพน ห้ามเลื่อน องค์ประกอบภาพต้องตรงกับรูปต้นฉบับทุกพิกเซล
- สัดส่วนภาพเท่ากับต้นฉบับ (ประมาณ 16:9) ความละเอียดอย่างน้อย 1280 × 720
- ความยาว 5–10 วินาที เฟรมแรกกับเฟรมสุดท้ายควรเหมือนกันที่สุด เพื่อให้วนลูปได้เนียน
- ไม่มีลายน้ำ ไม่ต้องมีเสียง
- ไฟล์ MP4 (H.264) ขนาดไม่เกิน 12 MB
- **ประตูร้าน (ด้านขวาของหน้าต่าง) ต้องอยู่นิ่ง ห้ามเปิด ห้ามขยับ** เพราะบนเว็บประตูเป็นปุ่มที่ตัดออกจากรูปมาเปิดเอง

**สิ่งที่ให้ขยับ:** ฝนตกหนัก น้ำหยดจากขอบกันสาด แอ่งน้ำบนพื้นหินกระเพื่อม ไฟโคมในร้านกับไฟถนนวูบไหวเบา ๆ ใบไม้เลื้อยไหวเล็กน้อย แมวดำกะพริบตาช้า ๆ หนึ่งครั้ง

**คำสั่ง (Prompt)**
```
Static locked-off camera, absolutely no camera movement, no zoom, no pan. Keep the exact composition of the input image. Heavy rain falling, water dripping from the striped awning, puddles rippling on the wet cobblestones, warm shop lights and the street lamp gently flickering, ivy leaves moving slightly in the wind, the black cat in the window blinks slowly once. The shop door stays closed and completely still. Seamless loop, the last frame matches the first frame. 8 seconds.
```

---

## ชิ้นที่ 2 · ภาพในร้าน: ร้านเดียวกับหน้าร้าน + ตู้พิเศษตรงกลาง

**เป้าหมาย:** คนที่ผลักประตูเข้าไปต้องรู้สึกว่าเข้ามาใน **ร้านเดียวกับที่เห็นผ่านกระจกใน `street.jpg`** แสงส้มทองอุ่นทั้งห้อง มีโคมตั้งโต๊ะโป๊ะผ้า ผนังเต็มไปด้วยชั้นหนังสือ หนังสือวางกองซ้อนบนโต๊ะ มีกระถางต้นไม้ และกระจกหน้าร้านที่ฝนไหลอยู่ ตรงกลางห้องคือ **ตู้หนังสือพิเศษจาก `bookcase.jpg`** ซึ่งเป็นตู้เดียวในร้านที่ยังเกือบว่าง

**แนบไปทั้งสองรูป:** `bookcase.jpg` (ใช้เป็นภาพหลักสำหรับ Expand) + `street.jpg` (ใช้เป็นตัวอย่างบรรยากาศ)

**เงื่อนไขที่ต้องผ่านทุกข้อ**
- ขยายผืนภาพเป็นแนวนอน 16:9 โดย **ความสูงเท่าเดิม (1448 px)** และ **วางตู้เดิมไว้กึ่งกลางพอดี**
  ขนาดที่แนะนำคือ 2576 × 1448 px (เติมด้านซ้ายและขวา ด้านละ 745 px)
- **รูปทรงและตำแหน่งของตู้ห้ามเปลี่ยน** ตัวตู้ ชั้น หนังสือ 1 เล่มบนชั้นบนสุด และตะเกียงต้องอยู่ตำแหน่งเดิม เพราะบนเว็บมีปุ่มกดวางทับอยู่
- **โทนแสงของตู้ปรับให้อุ่นขึ้นได้** ให้เข้ากับแสงส้มทองของร้าน (Harmonize lighting) แต่ห้ามขยับรูปทรง
- หน้าต่างเดิมในรูปที่เป็นท้องฟ้ากลางคืนสีน้ำเงิน และเตาผิงทางขวา **เปลี่ยนเป็นของในร้านได้** ไม่ต้องเก็บไว้
- ไม่มีตัวหนังสือที่อ่านได้ ไม่มีคน ไม่มีลายน้ำ
- ไฟล์ JPG หรือ PNG

**ด้านข้างควรมีอะไร** (ให้ตรงกับที่เห็นผ่านกระจกหน้าร้าน)
- **ซ้าย:** กระจกหน้าร้านบานใหญ่ที่มีน้ำฝนไหลลง มองออกไปเห็นไฟถนนเบลอ ๆ ข้างกระจกมีโต๊ะไม้ที่มีหนังสือกองซ้อนกัน โคมตั้งโต๊ะโป๊ะผ้าสีครีม และกระถางต้นไม้ มีแมวดำตัวเดียวกับหน้าร้านนั่งอยู่บนขอบหน้าต่าง
- **ขวา:** ชั้นหนังสือสูงจรดเพดานที่มีหนังสือเก่าเต็มทุกช่อง มีโคมไฟวางอยู่ในชั้น บันไดไม้สำหรับปีนหยิบหนังสือพิงอยู่ และหนังสือวางกองที่พื้น
- **ภาพรวม:** แสงส้มทองอุ่นจากโคมหลายดวง พื้นไม้เก่ากับพรม ร้านดูรก ๆ แต่น่าอยู่

**คำสั่ง (Prompt)**
```
Use the second attached image (the rainy bookshop exterior) as the reference for atmosphere, lighting and colors. Expand the first image (the bookcase) left and right to 16:9, keeping the bookcase exactly centered with the same shape, size and position, including the single book on the top shelf and the lantern. You may warm up the lighting on the bookcase so it matches the shop, but do not change its geometry. Turn the surroundings into the INSIDE of that same cozy bookshop at night: warm amber light from several fabric-shaded table lamps, walls lined with packed old bookshelves, stacks of books on wooden tables, potted plants. On the left, the large front shop window with rain streaming down the glass and blurry street lights outside, and the same black cat sitting on the window ledge. On the right, tall bookshelves up to the ceiling, a wooden library ladder, and books piled on the floor. Old wooden floor with a rug. The central bookcase is the only nearly empty shelf in the shop. Photorealistic, no people, no readable text.
```

**ถ้า AI ทำตามเงื่อนไขไม่ได้** (ตู้เปลี่ยนรูปทรงทุกครั้ง) ให้สร้างภาพในร้านใหม่ทั้งภาพตามคำสั่งด้านล่าง แล้วส่งมา ผมจะวัดตำแหน่งหนังสือในรูปใหม่แล้ววางปุ่มให้ตรงเอง
```
Use the attached rainy bookshop exterior as the reference for atmosphere, lighting and colors. Show the INSIDE of this same bookshop at night, straight-on view, 16:9. Warm amber light from fabric-shaded table lamps, walls full of old books, stacks of books on tables, potted plants, the rainy front window on the left with the same black cat on the ledge. In the center, one special dark carved wooden bookcase that is almost empty: only one old leather-bound book standing on the top shelf and a small brass candle lantern on the third shelf. Photorealistic, no people, no readable text.
```

---

## ชิ้นที่ 3 · วิดีโอในร้าน (ทำหลังได้ชิ้นที่ 2)

**ใช้รูป:** รูปที่ได้จากชิ้นที่ 2 (Image to Video)

**เงื่อนไขที่ต้องผ่านทุกข้อ**
- กล้องอยู่นิ่ง 100% องค์ประกอบภาพตรงกับรูปทุกพิกเซล
- **ตัวตู้ หนังสือบนชั้นบนสุด และการ์ดบนชั้นสอง ต้องอยู่นิ่งสนิท** เพราะบนเว็บเป็นปุ่มที่กดได้ ถ้าขยับ ปุ่มจะวางไม่ตรง
- ความยาว 5–10 วินาที วนลูปได้ ไม่มีลายน้ำ MP4 ไม่เกิน 12 MB

**สิ่งที่ให้ขยับ:** เปลวไฟในเตาผิง เปลวเทียนในตะเกียง ฝนนอกหน้าต่าง ไอจากถ้วยชาลอยขึ้นบาง ๆ ฝุ่นลอยช้า ๆ ในแสง

**คำสั่ง (Prompt)**
```
Static locked-off camera, no camera movement. Keep the exact composition. The fire in the fireplace crackles, the candle flame in the lantern flickers softly, rain streams down the window, thin steam rises from the tea cup, tiny dust particles drift slowly in the warm light. The bookcase, the books and the paper note stay completely still. Seamless loop. 8 seconds.
```

---

## ชิ้นที่ 4 · ภาพประกอบสารบัญ (ไม่บังคับ ทำทีหลังได้)

ใช้เป็นภาพบนการ์ดแต่ละบทนิยาย บทละ 1 รูป
- สัดส่วน 4:3 ขนาดประมาณ 1600 × 1200 px
- แนบ `street.jpg` ไปเป็นตัวอย่างสไตล์ทุกครั้ง ให้ภาพทุกบทดูเป็นโลกเดียวกัน

**คำสั่งต้นแบบ** (เปลี่ยนข้อความในวงเล็บเป็นฉากของบทนั้น)
```
Use the attached image as the style reference: same rainy night, warm amber light, photorealistic cinematic look. Scene: [describe the key moment of this chapter]. No readable text, no watermark. 4:3.
```

---

## ส่งงานกลับ
ส่งไฟล์ทั้งหมดกลับมาในแชตกับ Claude ตั้งชื่อตามนี้
- `street-loop.mp4`
- `bookcase-wide.jpg`
- `interior-loop.mp4`
- `chapter-1.jpg`, `chapter-2.jpg`, … (ถ้ามี)

**เช็กก่อนส่ง:** วางวิดีโอเทียบกับรูปต้นฉบับ แล้วสลับไปมา ภาพต้องไม่กระตุกหรือเลื่อนตำแหน่ง ถ้าเลื่อน ให้สร้างใหม่ และเน้นคำว่า "static camera" ให้มากขึ้น
