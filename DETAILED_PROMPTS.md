# 🎨 Tạo Prompts Chi Tiết - Depth & Layers

## 🎯 Vấn Đề Cũ

**Prompt cũ (đơn giản):**
```
forest, mountains, river, wildlife, sunset
```

**Kết quả:**
- ⚠️ Thiếu chi tiết
- ⚠️ Không có chiều sâu
- ⚠️ Scene phẳng, một góc nhìn

---

## ✅ Giải Pháp Mới

**Prompt mới (chi tiết với layers):**
```
tall pine trees, moss-covered rocks, small bushes, wildflowers (foreground),
deer grazing, winding river, forest floor (midground),
distant mountains, golden sunset sky, sun rays through canopy (background),
birds flying, fog in valley, atmospheric depth, multiple perspectives,
vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

**Kết quả:**
- ✅ Chi tiết cụ thể
- ✅ Có chiều sâu (3 layers)
- ✅ Nhiều góc nhìn
- ✅ Scene phong phú

---

## 📐 4 Nguyên Tắc Chi Tiết

### 1. **DEPTH LAYERS** (Chiều Sâu 3 Tầng)

#### Foreground (Cận cảnh):
```
moss-covered rocks, small bushes, wildflowers, grass, stones
```
- Gần camera nhất
- Chi tiết nhỏ, sắc nét
- Tạo độ sâu cho scene

#### Midground (Trung cảnh):
```
deer grazing, winding river, forest floor, fallen logs
```
- Chủ thể chính
- Điểm nhìn trung tâm
- Action diễn ra ở đây

#### Background (Xa cảnh):
```
distant mountains, golden sunset sky, clouds, horizon
```
- Xa camera nhất
- Tạo bối cảnh rộng
- Sky, mountains, distant objects

---

### 2. **MULTIPLE ANGLES** (Nhiều Góc Nhìn)

#### Từ dưới lên (Ground level):
```
grass, rocks at feet, ground texture, puddles
```

#### Tầm mắt (Eye level):
```
main subjects, people, animals, buildings
```

#### Từ trên xuống (Aerial):
```
birds flying overhead, clouds, tree canopy from above
```

#### Ví dụ kết hợp:
```
grass and flowers at ground level, deer at eye level, birds flying above,
→ Tạo cảm giác 3D, không phẳng!
```

---

### 3. **RICH DETAILS** (Chi Tiết Phong Phú)

#### ❌ Generic (Chung chung):
```
trees, water, animals
```

#### ✅ Specific (Cụ thể):
```
tall pine trees, moss-covered rocks, crystal clear stream,
deer with antlers, small rabbits, colorful wildflowers
```

#### ❌ Simple colors:
```
blue sky, green forest
```

#### ✅ Detailed colors:
```
golden sunset sky, emerald green forest, deep blue water,
orange and pink clouds, warm afternoon light
```

#### Add motion & life:
```
birds flying, water flowing, leaves rustling, deer grazing,
clouds drifting, sun rays moving through trees
```

---

### 4. **COMPOSITION** (Bố Cục)

#### Wide elements (Rộng):
```
landscape, panoramic view, vast horizon, open sky
```

#### Close elements (Gần):
```
detailed textures, small creatures, individual flowers, bark detail
```

#### Multiple focal points:
```
Không chỉ 1 chủ thể, mà nhiều điểm nhìn:
- Foreground: rocks
- Midground: deer + river
- Background: mountains + sunset
→ Mắt di chuyển qua nhiều layers!
```

---

## 🎨 Examples - Before vs After

### Example 1: Forest Scene

**❌ Before (simple):**
```
forest, trees, animals
```

**✅ After (detailed):**
```
tall pine trees, moss-covered rocks, small bushes, wildflowers, ferns,
deer grazing, winding river, forest floor, fallen logs, mushrooms,
distant mountains, golden hour lighting, sun rays through canopy,
birds flying, fog in valley, atmospheric depth, blue sky, clouds,
vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

---

### Example 2: Ocean Scene

**❌ Before (simple):**
```
ocean, fish, coral
```

**✅ After (detailed):**
```
colorful coral reef, sea anemones, small clownfish, starfish on rocks (foreground),
sea turtle swimming, school of tropical fish, jellyfish floating, seaweed swaying (midground),
deep blue ocean water, sunlight rays penetrating, distant horizon, waves above (background),
bubbles rising, underwater plants, sandy bottom, clear water, vibrant colors,
vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

---

### Example 3: Mountain Landscape

**❌ Before (simple):**
```
mountains, snow, sky
```

**✅ After (detailed):**
```
wildflower meadow, alpine grass, small rocks, hiking boots visible (foreground),
winding trail, small cabin, hikers walking, mountain stream, evergreen trees (midground),
snow-capped peaks, jagged cliffs, distant mountains fading into mist, vast blue sky (background),
morning light, shadows in valley, clouds around peaks, birds soaring, crisp air,
vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
```

---

## 🧪 Test Gemini

Chạy test script để xem Gemini tạo prompts chi tiết:

```bash
py -3.11 test_detailed_prompts.py
```

**Inputs test:**
1. forest mountains river wildlife sunset
2. ocean underwater scene
3. city skyline at night
4. desert landscape
5. space station

**Expected outputs:** Prompts dài, nhiều layers, chi tiết cụ thể!

---

## 🚀 Sử Dụng Trong App

### Workflow:

1. **User nhập simple idea:**
   ```
   forest scene
   ```

2. **Click "✨ Enhance với Gemini AI"**

3. **Gemini tạo detailed prompt:**
   ```
   tall pine trees, moss-covered rocks, wildflowers, deer grazing,
   winding river, distant mountains, golden sunset, birds flying,
   fog, atmospheric depth, vector art, Kurzgesagt, sharp focus,
   (HDR), (8k), (gigapixel), ((masterpiece))
   ```

4. **Generate image** → Ảnh có depth, layers, chi tiết!

---

## 📊 So Sánh Kết Quả

| Aspect | Simple Prompt | Detailed Prompt |
|--------|---------------|-----------------|
| Length | 5-10 từ | 30-50+ từ |
| Depth | 1 layer | 3 layers (FG/MG/BG) |
| Details | Generic | Specific |
| Perspectives | 1 góc | Multiple angles |
| Objects | Vài items | Many items |
| Result quality | ⚠️ OK | ✅ Rich & Deep |

---

## ✅ Summary

**Gemini AI giờ sẽ tạo prompts:**

1. ✅ **3 layers depth:** Foreground → Midground → Background
2. ✅ **Multiple angles:** Ground level, eye level, aerial
3. ✅ **Rich details:** Cụ thể, nhiều màu sắc, nhiều objects
4. ✅ **Good composition:** Wide + close elements, multiple focal points

**Kết quả:**
- Images có chiều sâu (không phẳng)
- Nhiều góc nhìn (3D feel)
- Chi tiết phong phú (nhiều layers)
- Bối cảnh rộng (panoramic)

**Test ngay:**
```bash
py -3.11 web_app.py
```

Nhập: "forest mountains river"
Click: "✨ Enhance với Gemini AI"
Xem Gemini tạo prompt chi tiết! 🎨
