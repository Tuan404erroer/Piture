# 🎯 CHỌN APP NÀO?

## Hiện Trạng

Bạn có **3 apps** trong project:

### ❌ 1. Streamlit (app.py) - KHÔNG DÙNG
```bash
py -3.11 -m streamlit run app.py
```
**Vấn đề:**
- ❌ Cứ disconnect/reconnect hoài
- ❌ st.rerun() gây infinite loop
- ❌ Connection error liên tục
- ❌ Không ổn định

**→ KHÔNG KHUYẾN NGHỊ!**

---

### ⚠️ 2. Flask Full (web_app.py) - CẦN RESTART MÁY
```bash
py -3.11 web_app.py
```
**Đặc điểm:**
- ✅ Ổn định, không disconnect
- ✅ Gemini AI sáng tạo kịch bản đầy đủ
- ✅ Full features
- ❌ **CẦN tăng Virtual Memory + RESTART máy**

**→ Dùng SAU KHI restart máy**

---

### ✅ 3. Flask LITE (web_app_lite.py) - DÙNG NGAY! ← KHUYẾN NGHỊ
```bash
py -3.11 web_app_lite.py
```
**Đặc điểm:**
- ✅ Tối ưu RAM MAX - chạy được NGAY
- ✅ Không cần restart máy
- ✅ Không cần tăng Virtual Memory (tạm thời)
- ✅ Ổn định, không disconnect
- ✅ Gemini AI vẫn hoạt động
- ⚠️ Default: 512x512, 30 steps (nhẹ hơn)
- ⚠️ Có thể load LoRA hoặc không (tùy RAM)

**→ DÙNG NGAY NÀY!** 🎯

---

## 🚀 QUYẾT ĐỊNH

### Dùng **Flask LITE** ngay bây giờ:

```bash
py -3.11 web_app_lite.py
```

**Ưu điểm:**
1. ✅ **Chạy được NGAY** - không cần restart
2. ✅ **Ổn định** - không có Streamlit disconnect issue
3. ✅ **Nhẹ nhất** - tối ưu RAM aggressive
4. ✅ **Có Gemini AI** - viết prompt tự động
5. ✅ **Có preset prompts** - dễ dùng
6. ✅ **Auto-retry** - nếu OOM sẽ giảm size tự động

**Nhược điểm:**
- ⚠️ Default 512x512 thay vì 768x768
- ⚠️ Default 30 steps thay vì 50
- ⚠️ Có thể không load được LoRA (nếu RAM quá ít)

**Kết luận:** ĐỦ DÙNG! Tạo ảnh OK, chất lượng acceptable!

---

## 📊 So Sánh 3 Apps

| Feature | Streamlit | Flask Full | **Flask LITE** |
|---------|-----------|------------|----------------|
| Ổn định | ❌ Disconnect | ✅ Stable | ✅ Stable |
| RAM usage | 🔴 High | 🟡 Medium | 🟢 Low |
| Cần restart | ⚠️ Yes | ⚠️ Yes | ✅ **NO** |
| Gemini AI | ✅ | ✅ | ✅ |
| Default size | 512x768 | 512x768 | 512x512 |
| Default steps | 50 | 50 | 30 |
| LoRA | ✅ | ✅ | ⚠️ Optional |
| Script gen | ✅ | ❌ | ❌ |
| **KHUYẾN NGHỊ** | ❌ | ⚠️ Later | ✅ **NOW** |

---

## 🎯 WORKFLOW KHUYẾN NGHỊ

### 🔥 Bước 1: Dùng Flask LITE NGAY (không cần restart)

```bash
# Đóng tất cả Chrome/apps khác
py -3.11 web_app_lite.py
```

**Test:**
1. Mở http://localhost:5000
2. Nhập: "ocean scene"
3. Click "✨ Enhance với Gemini AI"
4. Settings: 512x512, steps=30
5. Click "🚀 Tạo Ảnh"

**Nếu OK:** Dùng tiếp! ✅

**Nếu vẫn lỗi memory:** Giảm xuống 384x384, steps=20

---

### ⏰ Bước 2: Sau khi restart máy (optional)

Nếu sau này bạn restart máy (vì lý do khác), lúc đó:

1. **Tăng Virtual Memory** (lần đầu duy nhất):
   - Win+R → sysdm.cpl
   - Advanced → Settings → Advanced → Change
   - Custom: 8192 - 16384
   - Set → OK → Restart

2. **Chuyển sang Flask Full:**
   ```bash
   py -3.11 web_app.py
   ```

3. **Lợi ích:**
   - Tạo được 768x768
   - 50 steps (chất lượng cao hơn)
   - LoRA load chắc chắn

---

## 🔧 Nếu Flask LITE Vẫn Lỗi

### Lỗi: "Paging file too small"

**→ Không có cách nào khác, PHẢI restart:**

1. Tăng Virtual Memory (hướng dẫn ở trên)
2. Restart máy
3. Chạy Flask Full: `py -3.11 web_app.py`

### Lỗi: "CUDA out of memory"

**→ Giảm settings:**

- Size: 768→512→**384**
- Steps: 50→30→**20**
- Đóng Chrome trước khi generate

### Lỗi: Model không load được

**→ Xóa cache và thử lại:**

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\huggingface\hub\models--dreamlike*"
py -3.11 web_app_lite.py
```

---

## ✅ TÓM TẮT

### DÙNG NGAY:

```bash
py -3.11 web_app_lite.py
```

**Tại sao:**
1. ✅ Không cần restart máy
2. ✅ Ổn định (không như Streamlit)
3. ✅ Nhẹ nhất
4. ✅ Đủ dùng (512x512, 30 steps)

### SAU KHI RESTART:

```bash
py -3.11 web_app.py
```

**Tại sao:**
1. ✅ Chất lượng cao hơn (768x768, 50 steps)
2. ✅ LoRA chắc chắn load
3. ✅ Full power

---

## 📁 File Nào Là Gì

```
d:\HOC\PICTURE_AI\
├── app.py                    ← Streamlit (KHÔNG DÙNG)
├── web_app.py                ← Flask Full (SAU KHI RESTART)
├── web_app_lite.py           ← Flask LITE (DÙNG NGAY) ✅
├── templates/index.html      ← Flask UI
└── models/Kurzgesagt_v1.safetensors
```

---

## 🚀 HÀNH ĐỘNG NGAY

```bash
# 1. Đóng Chrome và apps khác
# 2. Chạy:
py -3.11 web_app_lite.py

# 3. Mở browser:
http://localhost:5000

# 4. Test với "ocean scene"
# 5. Generate với 512x512, steps=30
```

**Xong! Đơn giản vậy thôi!** 🎉
