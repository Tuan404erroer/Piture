# 🚀 Quick Start Guide

## Bắt đầu trong 5 phút!

### 1️⃣ Cài đặt (Lần đầu tiên)

**Windows - Cách đơn giản nhất:**
```bash
# Click đúp vào file:
install.bat
```

**Hoặc cách thủ công:**
```bash
# Tạo môi trường ảo
python -m venv venv
venv\Scripts\activate

# Cài đặt thư viện
pip install -r requirements.txt
```

⏱️ **Thời gian**: 5-10 phút (tùy tốc độ internet)

---

### 2️⃣ Chạy ứng dụng

**Windows - Cách đơn giản:**
```bash
# Click đúp vào file:
run.bat
```

**Hoặc thủ công:**
```bash
venv\Scripts\activate
streamlit run app.py
```

🌐 **Ứng dụng sẽ mở tại**: http://localhost:8501

---

### 3️⃣ Sử dụng

1. **Tải Model**: 
   - Nhấn nút "🚀 Tải Model" ở sidebar
   - Đợi 1-2 phút lần đầu tiên

2. **Chọn Preset hoặc viết prompt**:
   - Thử preset "🌌 Space Scene"
   - Hoặc tự viết prompt

3. **Tạo ảnh**:
   - Nhấn "🚀 Tạo Ảnh"
   - Đợi 30-60 giây
   - Tải về kết quả!

---

## 💡 Tips nhanh

### Prompt cơ bản:
```
kurzgesagt, vector art, [chủ đề của bạn], 
flat colors, sharp focus, masterpiece
```

### Thông số khuyến nghị:
- **Steps**: 40-50
- **CFG Scale**: 5-7
- **Resolution**: 512x512 (an toàn cho GPU 4GB)

### Chủ đề phù hợp:
- ✅ Vũ trụ, thiên nhiên, khoa học
- ✅ Động vật, phong cảnh
- ❌ Chân dung người thực
- ❌ Text/chữ

---

## 🔧 Gặp vấn đề?

### "CUDA out of memory"
→ Giảm resolution xuống 512x512

### "Model not found"
→ Kiểm tra file `models/Kurzgesagt_v1.safetensors` có tồn tại

### "Streamlit not found"
→ Chạy: `pip install -r requirements.txt`

---

## 📚 Tài liệu đầy đủ

Xem [README.md](README.md) để biết chi tiết!

---

**Chúc bạn tạo được những bức ảnh tuyệt đẹp! 🎨✨**
