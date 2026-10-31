# 🎨 Kurzgesagt AI Image Generator

Ứng dụng tạo ảnh AI với phong cách **Kurzgesagt - In a Nutshell** sử dụng Stable Diffusion và LoRA model.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Mục Lục

- [Giới thiệu](#-giới-thiệu)
- [Tính năng](#-tính-năng)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
- [Sử dụng](#-sử-dụng)
- [Thông số Model](#-thông-số-model)
- [Tips & Tricks](#-tips--tricks)
- [Xử lý lỗi](#-xử-lý-lỗi)

## 🎯 Giới thiệu

Ứng dụng này cho phép bạn tạo ra những bức ảnh với phong cách đặc trưng của **Kurzgesagt** - kênh YouTube nổi tiếng với các video animation giải thích khoa học. 

**Đặc điểm phong cách:**
- Vector art phẳng với màu sắc rực rỡ
- Không có viền hoặc lineart
- Chủ đề khoa học, thiên nhiên, vũ trụ
- Chú chim iconic của Kurzgesagt

## ✨ Tính năng

- 🎨 **Giao diện thân thiện**: Streamlit UI dễ sử dụng
- ⚡ **Tối ưu cho GPU yếu**: Hoạt động mượt mà trên RTX 2050 (4GB VRAM)
- 🎭 **Preset Prompts**: 6+ mẫu prompt có sẵn
- 🎛️ **Tùy chỉnh đầy đủ**: Steps, CFG Scale, Seed, LoRA strength
- 💾 **Tải về dễ dàng**: Download ảnh PNG chất lượng cao
- 📊 **Hiển thị thông số**: Xem lại các thông số đã sử dụng
- 🔄 **DPM++ 2M Karras**: Sampler chất lượng cao

## 💻 Yêu cầu hệ thống

### Tối thiểu:
- **OS**: Windows 10/11, Linux, macOS
- **Python**: 3.8 hoặc cao hơn
- **RAM**: 8GB
- **GPU**: NVIDIA RTX 2050 hoặc tương đương (4GB VRAM)
- **Disk**: 10GB trống (cho models)

### Khuyến nghị:
- **RAM**: 16GB+
- **GPU**: RTX 3060 trở lên (6GB+ VRAM)
- **Disk**: SSD để tải model nhanh hơn

## 🚀 Cài đặt

### Bước 1: Clone hoặc tải project

```bash
git clone https://github.com/your-username/kurzgesagt-ai-generator.git
cd kurzgesagt-ai-generator
```

### Bước 2: Tạo môi trường ảo (khuyến nghị)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

**Lưu ý**: Quá trình cài đặt PyTorch có thể mất vài phút.

### Bước 4: Kiểm tra CUDA (GPU)

```bash
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

Nếu hiển thị `CUDA available: True` là GPU đã sẵn sàng!

### Bước 5: Đặt LoRA model vào đúng vị trí

Đảm bảo file `Kurzgesagt_v1.safetensors` nằm trong thư mục:
```
PICTURE_AI/
├── models/
│   └── Kurzgesagt_v1.safetensors  ✅
├── app.py
├── config.py
└── requirements.txt
```

## 🎮 Sử dụng

### Khởi động ứng dụng:

```bash
streamlit run app.py
```

Ứng dụng sẽ mở tự động trong browser tại: `http://localhost:8501`

### Quy trình tạo ảnh:

1. **Tải Model**: Nhấn nút "🚀 Tải Model" trong sidebar (chỉ cần làm 1 lần)
2. **Chọn/Nhập Prompt**: Sử dụng preset hoặc tự viết prompt
3. **Điều chỉnh thông số**: Steps (40-50), CFG Scale (5-7), v.v.
4. **Tạo ảnh**: Nhấn "🚀 Tạo Ảnh"
5. **Tải về**: Nhấn "📥 Tải về ảnh" khi hài lòng

### Ví dụ Prompt:

```
starry, bird, Kurzgesagt bird, tree, star, using telescope, sunset, 
vector art, Kurzgesagt, sharp focus, (HDR), (8k), ((masterpiece))
```

### Negative Prompt mẫu:

```
lowres, blurry, low quality, bad body anatomy, letterbox, 
deformity, mutilated, malformed, amputee, watermark, signature
```

## 📊 Thông số Model

### LoRA Model Info:
- **Tên**: Kurzgesagt Style LoRA v1-DreamLike
- **Type**: LoRA (Low-Rank Adaptation)
- **Base Model**: Stable Diffusion 1.5
- **Size**: 144.08 MB (fp16 SafeTensor)
- **Training**: 848 steps, 8 epochs
- **CLIP Skip**: 1
- **Rating**: Very Positive (400 reviews)
- **Downloads**: 4,772+

### Trigger Words:
**Bắt buộc:**
- `kurzgesagt` hoặc `by kurzgesagt`
- `vector art`

**Tùy chọn:**
- `flat colors` - màu phẳng
- `no lineart` / `lineless` - không viền
- `Kurzgesagt bird` - chú chim iconic
- `sharp focus`, `HDR`, `8k`, `masterpiece` - nâng cao chất lượng

## 🎨 Tips & Tricks

### 1. Prompt Writing:

**✅ Nên:**
```
kurzgesagt, vector art, space, planets, galaxy, stars, 
flat colors, sharp focus, masterpiece
```

**❌ Không nên:**
```
realistic, photograph, 3D render, detailed lineart
```

### 2. Thông số khuyến nghị:

| Thông số | Giá trị khuyến nghị | Ghi chú |
|----------|-------------------|---------|
| Steps | 40-50 | Đủ cho chất lượng tốt |
| CFG Scale | 5-7 | Quá cao = oversaturated |
| LoRA Strength | 0.8-1.2 | 1.0 là chuẩn |
| Resolution | 512x512 | An toàn cho 4GB VRAM |
| Seed | Random | Hoặc dùng lại seed yêu thích |

### 3. Chủ đề phù hợp:

- ✅ **Khoa học**: atoms, DNA, space, evolution
- ✅ **Thiên nhiên**: forest, ocean, animals, landscapes
- ✅ **Vũ trụ**: planets, stars, galaxies, cosmos
- ✅ **Abstract**: concepts, time, philosophy
- ❌ **Portraits**: Không phù hợp với style này
- ❌ **Text**: Model không tạo text tốt

### 4. Tối ưu performance:

**Nếu bị thiếu VRAM:**
- Giảm resolution xuống 512x512
- Giảm steps xuống 40
- Đóng các ứng dụng khác

**Nếu tạo ảnh chậm:**
- Đảm bảo dùng GPU (CUDA)
- Kiểm tra không có app nặng chạy nền
- Lần đầu tiên sẽ chậm hơn (cache model)

## 🔧 Xử lý lỗi

### Lỗi: "CUDA out of memory"

**Giải pháp:**
```python
# Trong app.py, thêm vào sau khi load model:
pipe.enable_attention_slicing()
pipe.enable_vae_slicing()
```

Hoặc giảm resolution:
- 768x768 → 640x640 → 512x512

### Lỗi: "LoRA model not found"

**Kiểm tra:**
```bash
dir models\Kurzgesagt_v1.safetensors  # Windows
ls models/Kurzgesagt_v1.safetensors   # Linux/Mac
```

Đảm bảo file có đúng tên và đường dẫn.

### Lỗi: "CUDA not available"

**Cài đặt CUDA Toolkit:**
1. Tải từ: https://developer.nvidia.com/cuda-downloads
2. Cài đặt CUDA 11.8 hoặc 12.1
3. Cài lại PyTorch:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Lỗi: "Streamlit command not found"

**Giải pháp:**
```bash
python -m streamlit run app.py
```

Hoặc cài lại:
```bash
pip install --upgrade streamlit
```

## 📁 Cấu trúc Project

```
PICTURE_AI/
├── models/
│   ├── .cache/                      # Model cache (tự động tạo)
│   └── Kurzgesagt_v1.safetensors   # LoRA model
├── outputs/                         # Ảnh output (tự động tạo)
├── app.py                          # Ứng dụng Streamlit chính
├── config.py                       # Cấu hình và constants
├── requirements.txt                # Python dependencies
└── README.md                       # File này
```

## 🎯 Ví dụ Prompts

### 1. Space Scene với Kurzgesagt Bird:
```
Prompt: starry, bird, Kurzgesagt bird, tree, star, using telescope, 
        sunset, vector art, Kurzgesagt, sharp focus, (HDR), (8k), 
        (gigapixel), ((masterpiece))

Steps: 50
CFG: 5
Seed: 378096063
```

### 2. Tribe around Fire:
```
Prompt: starry, fire, torch, aborigines, night, moon, people, tribe, 
        vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), 
        ((masterpiece))

Steps: 50
CFG: 5
Seed: 3579084496
```

### 3. Ocean Life:
```
Prompt: ocean, underwater, coral reef, colorful fish, marine life, 
        deep sea, vector art, Kurzgesagt, flat colors, sharp focus, 
        ((masterpiece))

Steps: 45
CFG: 6
```

### 4. Scientific Concept:
```
Prompt: atoms, molecules, DNA helix, cells, microscopic view, 
        science, vector art, Kurzgesagt, flat colors, sharp focus, 
        ((masterpiece))

Steps: 50
CFG: 5.5
```

## 📈 Performance Benchmarks

Trên **RTX 2050** (4GB VRAM):
- 512x512, 40 steps: ~30-40 giây
- 512x512, 50 steps: ~40-50 giây
- 640x640, 50 steps: ~60-70 giây
- 768x768, 50 steps: ~90-120 giây

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork repo
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📝 License

Project này sử dụng license MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 🙏 Credits

- **Kurzgesagt LoRA Model**: [CivitAI - Kurzgesagt Style](https://civitai.com/models/...)
- **Base Model**: Dreamlike Diffusion 1.0
- **Framework**: Stable Diffusion, Diffusers, Streamlit
- **Inspiration**: Kurzgesagt - In a Nutshell YouTube Channel

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra phần [Xử lý lỗi](#-xử-lý-lỗi)
2. Xem [Issues](https://github.com/your-username/kurzgesagt-ai-generator/issues)
3. Tạo issue mới với thông tin chi tiết

## 🎉 Have Fun!

Chúc bạn tạo được những bức ảnh tuyệt đẹp với phong cách Kurzgesagt! 🎨✨

---

**Made with ❤️ for the AI Art Community**
