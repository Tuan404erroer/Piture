# 🔥 QUICK FIX - Memory Error

## ❌ Lỗi Hiện Tại
```
OSError: The paging file is too small for this operation to complete. (os error 1455)
```

## ⚠️ QUAN TRỌNG
**Đây là lỗi Windows system, KHÔNG PHẢI lỗi code!**
**BẮT BUỘC phải tăng Virtual Memory và RESTART máy!**

---

## ✅ CÁCH FIX (5 PHÚT)

### 📌 Bước 1: Mở System Properties

```
Nhấn: Windows + R
Gõ: sysdm.cpl
Enter
```

### 📌 Bước 2: Vào Performance Settings

```
1. Tab "Advanced"
2. Click "Settings..." (Performance section)
```

### 📌 Bước 3: Thay đổi Virtual Memory

```
1. Tab "Advanced" 
2. Click "Change..." (Virtual Memory)
3. BỎ TICK "Automatically manage..."
4. Chọn ổ C:
5. Chọn "Custom size"
6. Initial size: 8192
7. Maximum size: 16384
8. Click "Set"
9. Click "OK" (3 lần)
```

### 📌 Bước 4: RESTART MÁY

```
⚠️  BẮT BUỘC phải restart!
Không restart = lỗi vẫn còn!
```

---

## 🚀 Sau Khi Restart

### 1. Đóng các app khác
- Chrome/Edge
- Discord, Spotify
- Các game, apps nặng

### 2. Chạy app
```bash
py -3.11 web_app.py
```

### 3. Nếu thành công, sẽ thấy:
```
🔄 Loading base model...
Loading weights: 100%|████████████| 196/196
Loading pipeline components: 100%|████| 5/5
✅ Base model loaded
✅ Memory optimizations enabled

============================================================
🔄 Loading Kurzgesagt LoRA...
============================================================
✅ LoRA LOADED SUCCESSFULLY!
   (hoặc ❌ LoRA LOAD FAILED - OK, ta fix sau)

✅ Pipeline ready on cuda
GPU: NVIDIA GeForce RTX 2050

============================================================
🎨 Kurzgesagt AI + Gemini
============================================================
Server: http://localhost:5000
============================================================
```

---

## 🔍 Nếu Vẫn Lỗi Sau Khi Restart

### Check 1: Virtual Memory đã apply chưa?

```powershell
Get-WmiObject Win32_PageFileUsage
```

Phải thấy `AllocatedBaseSize` >= 8192

### Check 2: Đã restart máy chưa?

⚠️  **Không restart = setting không apply!**

### Check 3: RAM đủ không?

```
Task Manager → Performance → Memory
```

Cần tối thiểu **8GB RAM** (physical memory)

---

## 📊 Tại Sao Cần Virtual Memory?

```
Model size: 2GB
RAM overhead: 2-3GB
Windows: 2GB
Total cần: ~6-8GB

Nếu máy có 8GB RAM:
- Windows dùng: 2-3GB
- Apps khác: 1-2GB
- Còn lại: 3-5GB
→ KHÔNG ĐỦ cho model 2GB + overhead!

Virtual Memory = "RAM ảo" trên ổ cứng
→ Giải quyết vấn đề khi hết RAM thật
```

---

## ✅ TÓM TẮT

1. ⚙️  **Tăng Virtual Memory lên 8-16GB** (theo hướng dẫn trên)
2. 🔄 **RESTART máy** (BẮT BUỘC!)
3. 🚫 **Đóng Chrome và apps khác**
4. ▶️  **Chạy:** `py -3.11 web_app.py`

**Thời gian:** ~5 phút setup
**Cần làm:** 1 lần duy nhất
**Không có cách khác!** (Đây là lỗi Windows system)

---

## 🎯 CHECK LIST

- [ ] Đã tăng Virtual Memory (Initial: 8192, Max: 16384)
- [ ] Đã click "Set" và "OK"
- [ ] **ĐÃ RESTART MÁY** ← Quan trọng nhất!
- [ ] Đã đóng Chrome và apps khác
- [ ] Chạy `py -3.11 web_app.py`

Sau khi làm 5 bước trên → App sẽ chạy OK! 💪
