# 🔧 Fix MemoryError - "Paging File Too Small"

## ❌ Lỗi Gặp Phải

```
OSError: The paging file is too small for this operation to complete. (os error 1455)
MemoryError
```

**Nguyên nhân:** Máy bạn hết RAM khi load model (2GB+ model vào RAM)

---

## ✅ Giải Pháp (Chọn 1 trong 3)

### 🎯 Giải Pháp 1: TĂNG VIRTUAL MEMORY (KHUYẾN NGHỊ!)

#### Cách 1: Thủ Công (DễNhất)

1. **Nhấn `Win + R`** → Gõ `sysdm.cpl` → Enter
2. Tab **Advanced** → Click **Settings** (trong Performance)
3. Tab **Advanced** → Click **Change** (Virtual Memory)
4. **Uncheck** "Automatically manage paging file size"
5. Chọn drive C:
6. Chọn **Custom size**:
   - **Initial size:** `8192` MB
   - **Maximum size:** `16384` MB
7. Click **Set** → **OK** → **OK**
8. **RESTART** máy

#### Cách 2: PowerShell (Nhanh)

**Chạy PowerShell AS ADMINISTRATOR:**

```powershell
# Copy paste toàn bộ đoạn này:

$computersys = Get-WmiObject Win32_ComputerSystem -EnableAllPrivileges
$computersys.AutomaticManagedPagefile = $False
$computersys.Put()

$pagefile = Get-WmiObject -Query "Select * From Win32_PageFileSetting Where Name='C:\\pagefile.sys'"
if ($pagefile -eq $null) {
    # Tạo mới nếu chưa có
    $pagefile = ([WmiClass]"root\cimv2:Win32_PageFileSetting").CreateInstance()
    $pagefile.Name = "C:\pagefile.sys"
}
$pagefile.InitialSize = 8192
$pagefile.MaximumSize = 16384
$pagefile.Put()

Write-Host "✅ Virtual Memory set to 8-16 GB"
Write-Host "⚠️  RESTART máy để áp dụng!"
```

Sau đó **RESTART** máy!

---

### 🎯 Giải Pháp 2: ĐÓNG CÁC APP KHÁC

**Trước khi chạy `py -3.11 web_app.py`:**

1. Đóng **Chrome/Edge** (trình duyệt ăn RAM nhất)
2. Đóng **Discord, Spotify, Games**
3. Mở **Task Manager** (Ctrl+Shift+Esc) → End các app không cần
4. Chờ 10 giây cho RAM giải phóng
5. Chạy: `py -3.11 web_app.py`

---

### 🎯 Giải Pháp 3: SỬ DỤNG CODE ĐÃ TỐI ƯU (ĐÃ CẬP NHẬT!)

Tôi đã update `web_app.py` với các tối ưu:

#### Cải tiến đã thêm:

```python
# 1. Low CPU memory usage
pipeline = StableDiffusionPipeline.from_pretrained(
    ...,
    low_cpu_mem_usage=True,  # ← Giảm RAM usage
    variant="fp16"            # ← Dùng FP16 thay vì FP32
)

# 2. Memory optimizations
pipeline.enable_attention_slicing()      # Giảm VRAM
pipeline.enable_vae_slicing()           # Giảm VRAM
pipeline.enable_model_cpu_offload()     # Offload một phần sang CPU

# 3. Garbage collection
import gc
gc.collect()                            # Giải phóng RAM
torch.cuda.empty_cache()                # Clear VRAM
```

**Chạy lại:**
```bash
py -3.11 web_app.py
```

---

## 🧪 Test Từng Bước

### Bước 1: Check RAM hiện tại

```powershell
# PowerShell
Get-WmiObject Win32_ComputerSystem | Select-Object TotalPhysicalMemory

# Hoặc Task Manager → Performance → Memory
```

**Cần thiết:** 
- Minimum: 8GB RAM
- Recommended: 12GB+ RAM

### Bước 2: Check Paging File hiện tại

```powershell
Get-WmiObject Win32_PageFileUsage | Select-Object Name, AllocatedBaseSize, CurrentUsage
```

Nếu `AllocatedBaseSize` < 8192 → Cần tăng!

### Bước 3: Thử chạy với optimizations

```bash
py -3.11 web_app.py
```

**Nếu vẫn lỗi:** Làm Giải Pháp 1 (Tăng Virtual Memory) + RESTART

---

## 📊 So Sánh RAM Usage

| Method | RAM Usage | Speed |
|--------|-----------|-------|
| Default | ~6-8 GB | Nhanh |
| low_cpu_mem_usage=True | ~4-6 GB | Trung bình |
| + model_cpu_offload | ~3-5 GB | Chậm hơn |
| + Paging File 16GB | Stable | OK |

---

## ⚠️ Nếu Vẫn Lỗi

### Option A: Dùng Model Nhỏ Hơn

```python
# Thay vì dreamlike-diffusion-1.0 (2GB), dùng:
pipeline = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",  # Model nhỏ hơn
    ...
)
```

### Option B: Upgrade RAM

- RTX 2050 laptop thường có 8GB RAM
- Upgrade lên 16GB sẽ giải quyết hẳn

### Option C: Dùng Google Colab

Model quá lớn cho RAM → Run trên cloud (free):
- https://colab.research.google.com/
- Upload code lên Colab
- Dùng free GPU của Google

---

## 🚀 Quick Fix Checklist

- [ ] Đóng Chrome và apps khác
- [ ] Chạy `py -3.11 web_app.py` (đã có optimizations)
- [ ] Nếu lỗi → Tăng Virtual Memory (Giải Pháp 1)
- [ ] RESTART máy
- [ ] Chạy lại `py -3.11 web_app.py`
- [ ] Nếu vẫn lỗi → Check RAM < 8GB → Cần upgrade

---

## ✅ Sau Khi Fix Xong

Model sẽ load thành công và show:

```
🔄 Loading base model...
Loading weights: 100%|████████████| 196/196 [00:00<00:00]
Loading pipeline components: 100%|████| 5/5 [00:02<00:00]
✅ Base model loaded
✅ Memory optimizations enabled

============================================================
🔄 Loading Kurzgesagt LoRA...
============================================================
...
✅ Pipeline ready on cuda
GPU: NVIDIA GeForce RTX 2050

============================================================
🎨 Kurzgesagt AI + Gemini
============================================================
Server: http://localhost:5000
============================================================
```

---

## 📝 Tóm Tắt

**NGUYÊN NHÂN:** Model 2GB + Windows paging file nhỏ = MemoryError

**GIẢI PHÁP TỐT NHẤT:**
1. Tăng Virtual Memory lên 8-16GB (Giải Pháp 1)
2. RESTART máy
3. Chạy `py -3.11 web_app.py` (đã có optimizations)

**THỜI GIAN:** ~5 phút setup, 1 lần duy nhất!

🎯 **Try ngay Giải Pháp 1 và restart máy!**
