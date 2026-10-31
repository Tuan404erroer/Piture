# ✅ Hướng Dẫn Gemini AI - Tự Viết Kịch Bản Kurzgesagt

## 🎯 Tính Năng Mới

**Gemini AI giờ sẽ TỰ SÁNG TẠO kịch bản đầy đủ**, không chỉ format lại prompt!

### Ví Dụ Gemini Sáng Tạo:

#### Input: `"ocean scene"`
**Gemini tạo:**
```
ocean, sea, fish, coral, water, aquatic, blue background, jellyfish, 
underwater, sunlight rays, vector art, Kurzgesagt, sharp focus, 
(HDR), (8k), (gigapixel), ((masterpiece))
```

#### Input: `"ancient city"`  
**Gemini tạo:**
```
civilization, people, building, market, mayan pyramid, sky, day, 
temples, stone structures, crowd, vector art, Kurzgesagt, sharp focus, 
(HDR), (8k), (gigapixel), ((masterpiece))
```

#### Input: `"alien planet"`
**Gemini tạo:**
```
people, sun, sea, mountain, yellow sky, two sun, red sea, astronaut, 
exotic landscape, strange flora, vector art, Kurzgesagt, sharp focus, 
(HDR), (8k), (gigapixel), ((masterpiece))
```

---

## 📋 Format Chính Xác Như Model Samples

### Structure:
```
<lora:S1-Kurzgesagt_Dreamlike-000008:1>, [scene elements], vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

### Negative Prompt (tự động):
```
lowres, blurry, low quality, bad body anatomy, letterbox, deformity, mutilated, malformed, amputee, watermark, signature
```

### Settings (khớp samples):
- **Steps:** 50 (default)
- **CFG Scale:** 5.0
- **Sampler:** DPM++ 2M Karras
- **Size:** 512x768 (default)

---

## 🎨 Gemini Sáng Tạo Theo Quy Luật

### 1. **Concrete Objects** (Vật thể cụ thể)
✅ Pyramid, torch, astronaut, coral, jellyfish
❌ Không dùng abstract concepts

### 2. **Atmosphere** (Bầu không khí)
- Time: `day`, `night`, `sunset`, `dawn`
- Weather: `starry`, `cloudy`, `clear sky`
- Lighting: `fire`, `torch`, `sunlight rays`, `moonlight`

### 3. **Life & Characters** (Sống động)
- People: `people`, `crowd`, `tribe`, `civilization`
- Animals: `fish`, `bird`, `wildlife`
- Special: `Kurzgesagt bird` (character iconic)

### 4. **Rich Details** (Chi tiết phong phú)
- Colors: `yellow sky`, `red sea`, `blue background`
- Environment: `mountain`, `ocean`, `forest`, `space`
- Elements: `water`, `fire`, `rocks`, `trees`

### 5. **Story Frame** (Kịch bản có câu chuyện)
Mỗi prompt như 1 frame trong video Kurzgesagt:
- ✅ `astronaut, two sun, alien landscape` → Khám phá hành tinh lạ
- ✅ `aborigines, fire, night, moon, tribe` → Bộ lạc thời xưa
- ✅ `market, pyramid, civilization, people` → Văn minh cổ đại

---

## 🧪 Test Gemini Prompt Generation

### Chạy test script:
```bash
py -3.11 test_gemini_prompts.py
```

Script này sẽ test 5 inputs:
1. "ocean scene"
2. "ancient civilization"
3. "space exploration"
4. "forest animals"
5. "underwater world"

Xem output có đủ chi tiết không!

---

## 🚀 Workflow Hoàn Chỉnh

### Bước 1: Nhập ý tưởng ngắn
```
User input: "ocean scene"
```

### Bước 2: Gemini mở rộng thành kịch bản
```
Gemini tạo: ocean, sea, fish, coral, water, aquatic, blue background, 
jellyfish, underwater, sunlight rays, vector art, Kurzgesagt, 
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

### Bước 3: Thêm LoRA tag tự động
```
Full prompt: <lora:S1-Kurzgesagt_Dreamlike-000008:1>, ocean, sea, fish, 
coral, water, aquatic, blue background, jellyfish, underwater, 
sunlight rays, vector art, Kurzgesagt, sharp focus, (HDR), (8k), 
(gigapixel), ((masterpiece))
```

### Bước 4: Generate với settings chuẩn
- Steps: 50
- CFG: 5.0
- Size: 512x768
- Negative prompt: (tự động)

---

## ✅ So Sánh: Trước vs Sau

### ❌ TRƯỚC (Chỉ format lại):
```
User: "ocean"
Old Gemini: ocean, kurzgesagt, vector art, flat colors, sharp focus, 8k, masterpiece
```
→ Thiếu chi tiết, không có câu chuyện

### ✅ SAU (Tự sáng tạo kịch bản):
```
User: "ocean"  
New Gemini: ocean, sea, fish, coral, water, aquatic, blue background, 
jellyfish, underwater, sunlight rays, vector art, Kurzgesagt, 
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```
→ Đầy đủ chi tiết, có atmosphere, có life!

---

## 🎯 Các Preset Mẫu Trong UI

1. **🌌 Vũ trụ:** `space stars planets galaxy cosmic`
2. **🌲 Thiên nhiên:** `forest mountains river wildlife sunset`
3. **🔬 Khoa học:** `atoms molecules DNA cells science`
4. **🐦 Chim:** `bird tree sky clouds nature`

Nhấn preset → Gemini enhance → Generate!

---

## 📊 Kiểm Tra Kết Quả

Sau khi generate, UI sẽ hiển thị:
- ✅ **Seed used**
- ✅ **Steps, CFG, Size**
- ✅ **Full prompt đã dùng** (bao gồm LoRA tag)

Ví dụ output:
```
Seed: 3579084496
Steps: 50 | CFG: 5.0
Size: 512x768

Prompt đã dùng:
<lora:S1-Kurzgesagt_Dreamlike-000008:1>, starry, fire, torch, 
aborigines, night, moon, people, tribe, vector art, Kurzgesagt, 
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

---

## 🔄 Cách Sử Dụng

### Cách 1: Dùng Preset
1. Click preset (ví dụ: 🌌 Vũ trụ)
2. Click "✨ Enhance với Gemini AI"
3. Xem prompt được mở rộng
4. Click "🚀 Tạo Ảnh"

### Cách 2: Tự Nhập
1. Nhập ý tưởng: "underwater city"
2. Click "✨ Enhance với Gemini AI"
3. Gemini tạo: "underwater, city, buildings, ocean floor, fish, coral, 
   blue light, mysterious, architecture, vector art, Kurzgesagt..."
4. Click "🚀 Tạo Ảnh"

### Cách 3: Nhập Prompt Đầy Đủ Sẵn
Nếu bạn đã có prompt chi tiết, có thể bỏ qua Gemini:
```
starry, fire, torch, aborigines, night, moon, people, tribe, 
vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```
→ Click "🚀 Tạo Ảnh" luôn

---

## 🎨 Examples từ Model Samples

### Sample 1: Alien Planet
```
<lora:S1-Kurzgesagt_Dreamlike-000008:1>, people, sun, sea, mountain, 
yellow sky, two sun, red sea, astronaut, vector art, Kurzgesagt, 
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

### Sample 2: Tribal Night
```
<lora:S1-Kurzgesagt_Dreamlike-000008:1>, starry, fire, torch, 
aborigines, night, moon, people, tribe, vector art, Kurzgesagt, 
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

### Sample 3: Ancient Civilization
```
<lora:S1-Kurzgesagt_Dreamlike-000008:1>, civilization, people, 
building, market, mayan pyramid, sky, day, vector art, Kurzgesagt, 
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

Gemini giờ sẽ tạo prompts tương tự như thế này!

---

## ✅ Checklist

- [x] Gemini tự sáng tạo kịch bản đầy đủ
- [x] Format chính xác như model samples
- [x] Parentheses cho emphasis: `(HDR)`, `(8k)`, `((masterpiece))`
- [x] LoRA tag tự động: `<lora:S1-Kurzgesagt_Dreamlike-000008:1>`
- [x] Negative prompt chuẩn
- [x] UI hiển thị full prompt đã dùng
- [ ] **CHỜ BẠN TEST:** `py -3.11 web_app.py`

---

## 🚀 Chạy Ngay!

```bash
py -3.11 web_app.py
```

Mở http://localhost:5000 và test:
1. Nhập: "ocean world"
2. Click "✨ Enhance với Gemini AI"
3. Xem Gemini tạo prompt chi tiết
4. Click "🚀 Tạo Ảnh"
5. Check kết quả có giống samples không!
