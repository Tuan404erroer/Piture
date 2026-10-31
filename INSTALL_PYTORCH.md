# 🔥 Hướng dẫn cài đặt PyTorch cho Python 3.14

Python 3.14 là version rất mới, cần cài đặt PyTorch theo cách đặc biệt.

## 🎯 Bước 1: Kiểm tra GPU

Mở PowerShell và chạy:
```powershell
nvidia-smi
```

Nếu thấy thông tin GPU RTX 2050 → Bạn có CUDA  
Nếu báo lỗi → Không có CUDA, dùng CPU

---

## 🚀 Bước 2: Cài đặt PyTorch

### Option A: Có GPU (CUDA) - KHUYẾN NGHỊ

```powershell
# CUDA 11.8 (tương thích tốt với RTX 2050)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Option B: Có GPU (CUDA 12.1+) - Nếu bạn đã cài CUDA 12

```powershell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

### Option C: Không có GPU (CPU only)

```powershell
pip install torch torchvision
```

⚠️ **Lưu ý**: CPU sẽ RẤT CHẬM (5-10 phút/ảnh)

---

## 📦 Bước 3: Cài đặt các thư viện còn lại

```powershell
pip install -r requirements.txt
```

---

## ✅ Bước 4: Kiểm tra cài đặt

```powershell
python check_system.py
```

Script này sẽ kiểm tra:
- ✅ Python version
- ✅ PyTorch đã cài chưa
- ✅ CUDA có hoạt động không
- ✅ Model files
- ✅ GPU specs

---

## 🔍 Xác định CUDA version của bạn

Nếu chưa biết CUDA version:

```powershell
# Kiểm tra CUDA
nvcc --version
```

Hoặc:

```powershell
nvidia-smi
```

Dòng "CUDA Version: X.X" sẽ cho biết version.

---

## 🎯 Khuyến nghị cho RTX 2050

RTX 2050 hỗ trợ tốt nhất với:
- **CUDA 11.8** hoặc **CUDA 12.1**
- **PyTorch 2.0+**

Nên dùng lệnh:
```powershell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

---

## 🐛 Xử lý lỗi thường gặp

### Lỗi: "No matching distribution"

**Nguyên nhân**: Python 3.14 quá mới, PyTorch chưa có wheel

**Giải pháp**:
1. Cài PyTorch nightly build:
```powershell
pip install --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu118
```

2. Hoặc dùng Python 3.11 (ổn định hơn):
```powershell
# Tải Python 3.11 từ python.org
# Tạo lại venv với Python 3.11
py -3.11 -m venv venv
```

### Lỗi: "CUDA not available" sau khi cài

**Kiểm tra**:
```python
import torch
print(torch.cuda.is_available())
```

Nếu `False`:
1. Cài lại PyTorch với CUDA:
```powershell
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

2. Cài CUDA Toolkit từ: https://developer.nvidia.com/cuda-downloads

### Lỗi: "DLL load failed"

**Giải pháp**:
1. Cài Visual C++ Redistributable:
   https://aka.ms/vs/17/release/vc_redist.x64.exe

2. Khởi động lại máy

---

## 📋 Quy trình cài đặt đầy đủ

### Cho Python 3.14 (EXPERIMENTAL):

```powershell
# 1. Tạo virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Upgrade pip
python -m pip install --upgrade pip

# 3. Cài PyTorch (CUDA 11.8)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# 4. Cài các thư viện còn lại
pip install -r requirements.txt

# 5. Kiểm tra
python check_system.py
```

### Cho Python 3.11 (KHUYẾN NGHỊ - ỔN ĐỊNH):

```powershell
# 1. Tải Python 3.11: https://www.python.org/downloads/
# 2. Cài đặt Python 3.11
# 3. Tạo venv với Python 3.11
py -3.11 -m venv venv
venv\Scripts\activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Cài PyTorch (CUDA 11.8)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# 6. Cài các thư viện còn lại
pip install -r requirements.txt

# 7. Kiểm tra
python check_system.py
```

---

## 🎉 Hoàn thành!

Sau khi cài đặt xong, chạy:

```powershell
streamlit run app.py
```

Hoặc:

```powershell
run.bat
```

---

## 📞 Cần trợ giúp?

1. Chạy `python check_system.py` để xem vấn đề
2. Đọc phần "Xử lý lỗi" trong README.md
3. Kiểm tra log lỗi cụ thể

---

**Good luck! 🚀**
