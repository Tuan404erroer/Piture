# 🔧 Fix Streamlit "TypeError: Failed to fetch"

## ❌ Lỗi Gặp Phải

```
192.168.1.100:5000 says
Lỗi kết nối: TypeError: Failed to fetch
```

## 🔍 Nguyên Nhân

Lỗi này xảy ra khi:
1. **App bị crash do hết RAM** - Memory error khi tạo ảnh
2. **Gemini API timeout** - Model name sai
3. **LoRA loading fail** - File không tồn tại

---

## ✅ ĐÃ FIX

### 1. **Gemini Model Name** ✅
```python
# Đã sửa trong gemini_service.py
GEMINI_MODEL = "gemini-1.5-flash"  # Đổi từ "gemini-3.1-flash-lite"
```

### 2. **Memory Optimization** ✅
```python
# Đã thêm vào pipeline_service.py
- low_cpu_mem_usage=True
- gc.collect() trước khi load
- torch.cuda.empty_cache()
```

### 3. **Error Handling** ✅
```python
# Đã thêm vào app.py
- MemoryError → hiển thị lỗi rõ ràng
- CUDA OOM → suggest giảm resolution
- Traceback detail trong expander
```

---

## 🚀 Cách Chạy Lại

### Bước 1: Đóng Streamlit Hiện Tại

```powershell
# Nếu Streamlit đang chạy, nhấn Ctrl+C trong terminal
# Hoặc đóng cửa sổ terminal
```

### Bước 2: Đảm Bảo Virtual Memory Đã Tăng

⚠️ **QUAN TRỌNG:** Nếu chưa tăng Virtual Memory và restart máy, làm theo `QUICK_FIX.md`:
- Initial size: 8192 MB
- Maximum size: 16384 MB
- **RESTART MÁY**

### Bước 3: Đóng Các App Khác

- Đóng Chrome/Edge
- Đóng Discord, Spotify
- Mở Task Manager → End các app không cần

### Bước 4: Chạy Streamlit

```bash
py -3.11 -m streamlit run app.py
```

### Bước 5: Test Từng Bước

1. **Load Model:**
   - Click "🚀 Tải Model + LoRA"
   - Đợi ~1-2 phút
   - Phải thấy: "✅ Model + LoRA sẵn sàng!"

2. **Test Gemini:**
   - Nhập: "bird tree sky clouds nature"
   - Click "✨ AI viết prompt (Gemini)"
   - Phải thấy prompt đầy đủ xuất hiện

3. **Test Generate:**
   - Giảm resolution xuống: **512x512** (nếu lỗi memory)
   - Giảm steps xuống: **30** (để test nhanh)
   - Click "🚀 Tạo Ảnh"

---

## ⚠️ Nếu Vẫn Lỗi

### Lỗi 1: "Failed to fetch" khi Load Model

**Nguyên nhân:** Hết RAM

**Fix:**
1. Kiểm tra đã tăng Virtual Memory chưa:
   ```powershell
   Get-WmiObject Win32_PageFileUsage
   ```
   Phải thấy `AllocatedBaseSize` >= 8192

2. Nếu chưa → Làm theo `QUICK_FIX.md` và **RESTART MÁY**

3. Nếu đã tăng mà vẫn lỗi → RAM < 8GB → Cần upgrade RAM

### Lỗi 2: "Failed to fetch" khi Generate

**Nguyên nhân:** VRAM/RAM hết khi tạo ảnh

**Fix:**
- Giảm resolution: 768x768 → **512x512**
- Giảm steps: 50 → **30**
- Đóng tất cả apps khác trước khi generate

### Lỗi 3: Gemini API Error

**Nguyên nhân:** API key sai hoặc model name sai

**Fix:**
1. Check API key trong `.streamlit/secrets.toml`:
   ```toml
   GOOGLE_API_KEY = "AIzaSy..."
   ```

2. Test API key:
   ```python
   py -3.11 -c "from google import genai; client = genai.Client(api_key='YOUR_KEY'); print('OK')"
   ```

### Lỗi 4: LoRA Not Found

**Nguyên nhân:** File LoRA không tồn tại

**Fix:**
1. Check file tồn tại:
   ```powershell
   Test-Path "models\Kurzgesagt_v1.safetensors"
   ```

2. Nếu không có → Download từ CivitAI và đặt vào `models/`

---

## 📊 System Requirements

### Tối Thiểu:
- **RAM:** 8GB physical
- **VRAM:** 4GB (RTX 2050)
- **Virtual Memory:** 8-16GB
- **Storage:** 5GB free

### Khuyến Nghị:
- **RAM:** 16GB
- **VRAM:** 6GB+
- **Virtual Memory:** 16GB
- **Storage:** 10GB free

---

## 🎯 Quick Troubleshooting

| Lỗi | Nguyên nhân | Fix |
|-----|-------------|-----|
| Failed to fetch (load) | Hết RAM | Tăng Virtual Memory + restart |
| Failed to fetch (generate) | Hết VRAM/RAM | Giảm resolution/steps |
| Gemini error | Model name sai | Đã fix → chạy lại app |
| LoRA not found | File không có | Download và đặt vào models/ |
| CUDA OOM | VRAM hết | Giảm 768→512, steps 50→30 |

---

## ✅ Checklist

- [ ] Đã sửa gemini_service.py (model name)
- [ ] Đã tăng Virtual Memory (8-16GB)
- [ ] Đã restart máy
- [ ] Đóng Chrome và apps khác
- [ ] Chạy: `py -3.11 -m streamlit run app.py`
- [ ] Load model thành công
- [ ] Test Gemini OK
- [ ] Test generate với 512x512, steps=30

---

## 🚀 Commands

```bash
# Stop app hiện tại
Ctrl+C

# Check Virtual Memory
Get-WmiObject Win32_PageFileUsage

# Check RAM
Get-WmiObject Win32_ComputerSystem | Select TotalPhysicalMemory

# Run app
py -3.11 -m streamlit run app.py

# Test Gemini
py -3.11 -c "from gemini_service import enhance_prompt; print(enhance_prompt('test'))"
```

---

**Tóm tắt:** 
1. ✅ Đã fix Gemini model name
2. ✅ Đã thêm memory optimizations
3. ✅ Đã thêm better error handling
4. ⚠️ BẮT BUỘC: Tăng Virtual Memory + restart máy
5. 🚀 Chạy lại: `py -3.11 -m streamlit run app.py`
