"""
Kiểm tra xem có gọi được model không
"""

import torch
from diffusers.pipelines import StableDiffusionPipeline
from diffusers.schedulers import DPMSolverMultistepScheduler
import os

print("="*60)
print("KIỂM TRA MODEL")
print("="*60)

# Check CUDA
print(f"\n1. CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"   GPU: {torch.cuda.get_device_name(0)}")

# Check LoRA file
lora_path = "models/Kurzgesagt_v1.safetensors"
print(f"\n2. LoRA file exists: {os.path.exists(lora_path)}")
if os.path.exists(lora_path):
    size_mb = os.path.getsize(lora_path) / (1024*1024)
    print(f"   Size: {size_mb:.2f} MB")

# Try load base model
print(f"\n3. Loading base model...")
try:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    pipe = StableDiffusionPipeline.from_pretrained(
        "dreamlike-art/dreamlike-diffusion-1.0",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None
    )
    print("   ✅ Base model loaded!")
    
    # Setup scheduler
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(
        pipe.scheduler.config,
        algorithm_type="dpmsolver++",
        use_karras_sigmas=True
    )
    print("   ✅ Scheduler configured!")
    
    # Try load LoRA - QUAN TRỌNG NHẤT
    print(f"\n4. Trying to load LoRA...")
    try:
        # Thử method 1
        pipe.load_lora_weights("models", weight_name="Kurzgesagt_v1.safetensors")
        print("   ✅ LoRA loaded with method 1!")
    except Exception as e1:
        print(f"   ❌ Method 1 failed: {e1}")
        
        # Thử method 2
        try:
            from safetensors.torch import load_file
            state_dict = load_file(lora_path)
            print(f"   Keys in LoRA: {list(state_dict.keys())[:3]}...")
            print("   ❌ LoRA file OK but cannot apply to pipeline")
        except Exception as e2:
            print(f"   ❌ Method 2 failed: {e2}")
    
    # Move to device
    pipe = pipe.to(device)
    print(f"\n5. Pipeline moved to {device}")
    
    # Test generation
    print(f"\n6. Testing generation...")
    import random
    seed = random.randint(0, 2147483647)
    generator = torch.Generator(device=device).manual_seed(seed)
    
    prompt = "kurzgesagt, bird, tree, vector art, flat colors, no lineart, masterpiece"
    negative = "realistic, photograph, detailed lineart"
    
    image = pipe(
        prompt=prompt,
        negative_prompt=negative,
        num_inference_steps=20,
        guidance_scale=5.0,
        width=512,
        height=512,
        generator=generator
    ).images[0]
    
    print("   ✅ Generation successful!")
    image.save("test_output.png")
    print("   Saved to: test_output.png")
    
    print("\n" + "="*60)
    print("KẾT LUẬN:")
    print("- Model chạy được ✅")
    print("- LoRA KHÔNG load được ❌ (Đây là vấn đề!)")
    print("- Ảnh sẽ KHÔNG có style Kurzgesagt đặc trưng")
    print("="*60)
    
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()
