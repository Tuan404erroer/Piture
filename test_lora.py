"""Test if LoRA can be loaded"""
import torch
from diffusers.pipelines import StableDiffusionPipeline
from diffusers.schedulers import DPMSolverMultistepScheduler

print("=" * 60)
print("KURZGESAGT LORA TEST")
print("=" * 60)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\n1. Device: {device}")

print("\n2. Loading base model...")
pipeline = StableDiffusionPipeline.from_pretrained(
    "dreamlike-art/dreamlike-diffusion-1.0",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    safety_checker=None
)
pipeline = pipeline.to(device)
print("   ✅ Base model loaded")

print("\n3. Testing LoRA load methods...")

# Method 1: Standard load_lora_weights
print("\n   Method 1: pipeline.load_lora_weights('models', weight_name='Kurzgesagt_v1.safetensors')")
try:
    pipeline.load_lora_weights("models", weight_name="Kurzgesagt_v1.safetensors")
    print("   ✅ SUCCESS!")
except Exception as e:
    print(f"   ❌ FAILED: {type(e).__name__}: {e}")

print("\n" + "=" * 60)
print("Test complete!")
print("=" * 60)
