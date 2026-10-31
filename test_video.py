import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
import gc
import os

def run_test():
    print("="*60)
    print("🚀 BẮT ĐẦU TEST STABLE VIDEO DIFFUSION (SVD) TRÊN 4GB VRAM")
    print("="*60)

    print("\n1. Đang kết nối tới máy chủ HuggingFace...")
    print("⏳ Nếu đây là lần đầu chạy, máy sẽ tải khoảng 9GB dữ liệu (tuỳ tốc độ mạng).")
    print("⏳ Từ lần sau sẽ nạp thẳng từ ổ cứng không cần tải lại.\n")
    
    # Tải pipeline (chỉ tải bản fp16 để giảm dung lượng xuống một nửa)
    try:
        pipe = StableVideoDiffusionPipeline.from_pretrained(
            "stabilityai/stable-video-diffusion-img2vid", 
            torch_dtype=torch.float16, 
            variant="fp16"
        )
    except Exception as e:
        print(f"❌ Lỗi khi tải model: {e}")
        return

    print("\n2. Đang áp dụng các kỹ thuật chắt bóp bộ nhớ (CPU Offloading & Chunking)...")
    # Các lệnh BẮT BUỘC để chạy trên 4GB VRAM
    if torch.cuda.is_available():
        pipe.enable_model_cpu_offload()      # Đẩy bớt gánh nặng sang RAM 16GB
    else:
        print("⚠️ Không tìm thấy GPU (CUDA)! Sẽ chạy hoàn toàn trên CPU (rất chậm).")
        pipe.to("cpu")
    pipe.unet.enable_forward_chunking()  # Xử lý từng mẩu nhỏ thay vì cả cục
    
    # 3. Chuẩn bị ảnh đầu vào
    print("\n3. Đang tải ảnh mẫu (Rocket) để làm video...")
    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/svd/rocket.png"
    image = load_image(image_url)
    image = image.resize((512, 512)) # Ép độ phân giải nhỏ để tránh văng VRAM

    print("\n4. 🎬 BẮT ĐẦU NỘI SUY VIDEO (CÓ THỂ MẤT TỪ 10 ĐẾN 20 PHÚT)...")
    print("👉 Hãy để máy chạy và có thể đi pha một tách cà phê nhé ☕")
    
    try:
        # Bắt đầu sinh video
        generator = torch.manual_seed(42)
        frames = pipe(
            image, 
            decode_chunk_size=1, # Cực kỳ quan trọng: giải mã từng khung hình 1 để không nổ card
            generator=generator,
            num_frames=14 # Tạo 14 khung hình
        ).frames[0]

        # Lưu thành file MP4
        output_file = "test_svd_video.mp4"
        export_to_video(frames, output_file, fps=7)
        print(f"\n✅ THÀNH CÔNG RỰC RỠ! Video đã được lưu thành: {output_file}")
    except Exception as e:
        print(f"\n❌ Ối, máy đã hết hơi (VRAM/RAM quá tải) hoặc có lỗi xảy ra:")
        print(e)
    
    # Dọn dẹp
    del pipe
    gc.collect()
    torch.cuda.empty_cache()

if __name__ == "__main__":
    run_test()
