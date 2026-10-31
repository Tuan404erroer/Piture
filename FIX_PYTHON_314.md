# 🔧 Sửa lỗi cài đặt cho Python 3.14

## ⚠️ Vấn đề

Python 3.14 là version rất mới (beta/alpha), nhiều thư viện ML chưa có wheel sẵn.

## ✅ Giải pháp nhanh nhất

### Option 1: Cài PyTorch trước (KHUYẾN NGHỊ)

```powershell
# Kích hoạt virtual environment
venv\Scripts\activate

# Cài PyTorch với CUDA 11.8 (cho RTX 2050)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Sau đó cài các thư viện còn lại
pip install streamlit diffusers transformers accelerate safetensors Pillow numpy scipy
```

### Option 2: Dùng file install_simple.bat

```powershell
# Chỉ cần chạy:
install_simple.bat
```

File này sẽ tự động:
1. Tạo virtual environment
2. Cài PyTorch với CUDA
3. Cài các thư viện khác
4. Chạy system check

---

## 📋 Lệnh cài đặt đầy đủ (Copy & Paste)

Mở **PowerShell** trong thư mục `PICTURE_AI`:

```powershell
# 1. Tạo và kích hoạt venv
python -m venv venv
venv\Scripts\activate

# 2. Upgrade pip
python -m pip install --upgrade pip

# 3. Cài PyTorch (CUDA 11.8 - cho RTX 2050)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# 4. Cài Streamlit
pip install streamlit

# 5. Cài Diffusion libraries
pip install diffusers transformers accelerate

# 6. Cài utilities
pip install safetensors Pillow numpy scipy

# 7. Kiểm tra cài đặt
python check_system.py

# 8. Chạy app
streamlit run app.py
```

---

## 🎯 Nếu vẫn gặp lỗi

### Lỗi: "No matching distribution for torch"

**Thử nightly build:**
```powershell
pip install --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu118
```

### Lỗi: "DLL load failed" hoặc "Module not found"

**Cài Visual C++ Redistributable:**
1. Tải: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Cài đặt
3. Khởi động lại máy

### Lỗi: "CUDA not available"

**Kiểm tra GPU:**
```powershell
nvidia-smi
```

Nếu không thấy GPU:
- Cập nhật driver NVIDIA: https://www.nvidia.com/Download/index.aspx
- Khởi động lại máy

---

## 🔄 Option: Dùng Python 3.11 (Ổn định hơn)

Nếu Python 3.14 gặp quá nhiều vấn đề:

1. **Tải Python 3.11**: https://www.python.org/downloads/release/python-3119/
2. **Cài đặt** Python 3.11
3. **Tạo venv mới** với Python 3.11:

```powershell
# Xóa venv cũ
rmdir /s /q venv

# Tạo venv mới với Python 3.11
py -3.11 -m venv venv

# Kích hoạt
venv\Scripts\activate

# Cài đặt
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
pip install streamlit diffusers transformers accelerate safetensors Pillow numpy scipy
```

---

## ✅ Kiểm tra sau khi cài

```powershell
python check_system.py
```

Output mong đợi:
```
✅ Python version OK
✅ CUDA is available!
✅ GPU name: NVIDIA GeForce RTX 2050
✅ LoRA model found
✅ All packages installed
```

---

## 🚀 Chạy ứng dụng

```powershell
streamlit run app.py
```

Hoặc:

```powershell
run.bat
```

---

## 📞 Vẫn cần trợ giúp?

1. Chạy `python check_system.py` và gửi output
2. Kiểm tra Python version: `python --version`
3. Kiểm tra CUDA: `nvidia-smi`
4. Đọc file `INSTALL_PYTORCH.md` để biết thêm chi tiết

---

**Good luck! 🎨**
