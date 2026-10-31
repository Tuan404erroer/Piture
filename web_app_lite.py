"""
Flask App - LITE VERSION (giảm RAM usage tối đa)
Dùng khi chưa tăng Virtual Memory
"""
from flask import Flask, render_template, request, jsonify
import torch
from diffusers.pipelines import StableDiffusionPipeline
from diffusers.schedulers import DPMSolverMultistepScheduler
import random
from io import BytesIO
import base64
import google.generativeai as genai
import gc
import os

app = Flask(__name__)

# Load API key
with open('.streamlit/secrets.toml', 'r') as f:
    api_key = f.read().split('=')[1].strip().strip('"')
genai.configure(api_key=api_key)

gemini_model = genai.GenerativeModel('gemini-1.5-flash')

pipeline = None
device = None

def enhance_prompt_with_gemini(user_prompt):
    """Gemini AI - simplified for speed"""
    system_prompt = f"""Create Kurzgesagt-style image prompt from: "{user_prompt}"

Format: [scene objects], vector art, Kurzgesagt, sharp focus, (HDR), (8k), ((masterpiece))

Examples:
- ocean: ocean, sea, fish, coral, water, vector art, Kurzgesagt, sharp focus, (HDR), (8k), ((masterpiece))
- space: starry, planets, astronaut, cosmic, vector art, Kurzgesagt, sharp focus, (HDR), (8k), ((masterpiece))

Return ONLY the prompt, no explanation."""

    try:
        response = gemini_model.generate_content(system_prompt)
        enhanced = response.text.strip().replace('*', '').replace('`', '').replace('"', '')
        if "vector art" not in enhanced:
            enhanced += ", vector art, Kurzgesagt, sharp focus, (HDR), (8k), ((masterpiece))"
        return enhanced
    except Exception as e:
        print(f"Gemini error: {e}")
        return f"{user_prompt}, vector art, Kurzgesagt, sharp focus, (HDR), (8k), ((masterpiece))"

def load_model_once():
    global pipeline, device
    
    print("\n" + "="*60)
    print("🔄 LITE MODE - Optimized for RTX 2050 (4GB VRAM)")
    print("="*60)
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # AGGRESSIVE memory cleanup
    gc.collect()
    if device == "cuda":
        torch.cuda.empty_cache()
    
    # Force unload any existing models
    import sys
    for module in list(sys.modules.keys()):
        if 'transformers' in module or 'diffusers' in module:
            if module not in ['transformers', 'diffusers']:
                try:
                    del sys.modules[module]
                except:
                    pass
    
    print("📥 Loading from cache...")
    
    # Load với tối ưu memory MAX cho 4GB VRAM
    pipeline = StableDiffusionPipeline.from_pretrained(
        "dreamlike-art/dreamlike-diffusion-1.0",
        torch_dtype=torch.float16,  # FP16 để giảm VRAM
        safety_checker=None,
        low_cpu_mem_usage=True,
        use_safetensors=True,
    )
    
    print("✅ Base model loaded")
    
    # Simple scheduler
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
        pipeline.scheduler.config,
        algorithm_type="dpmsolver++",
        use_karras_sigmas=True
    )
    
    # Move to device ONCE
    pipeline = pipeline.to(device)
    
    # CRITICAL: Memory optimizations for 4GB VRAM
    if device == "cuda":
        # Slice attention thành nhiều phần nhỏ
        pipeline.enable_attention_slicing(slice_size=1)  # Max slicing
        
        # VAE slicing
        pipeline.enable_vae_slicing()
        
        # QUAN TRỌNG: Enable CPU offload để giảm VRAM
        # UNet (phần nặng nhất) sẽ được offload sang CPU khi không dùng
        pipeline.enable_model_cpu_offload()
        
        # Hoặc dùng sequential CPU offload (aggressive hơn)
        # pipeline.enable_sequential_cpu_offload()
        
        print("✅ 4GB VRAM optimizations enabled:")
        print("   - Attention slicing: ON")
        print("   - VAE slicing: ON")
        print("   - Model CPU offload: ON")
    
    print(f"✅ Device: {device}")
    if device == "cuda":
        gpu_name = torch.cuda.get_device_name(0)
        vram_total = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"   GPU: {gpu_name}")
        print(f"   VRAM: {vram_total:.1f}GB")
    
    # LoRA - optional (có thể không load được với 4GB VRAM)
    lora_loaded = False
    lora_path = "models/Kurzgesagt_v1.safetensors"
    if os.path.exists(lora_path):
        try:
            print("\n🔄 Loading LoRA...")
            pipeline.load_lora_weights("models", weight_name="Kurzgesagt_v1.safetensors")
            lora_loaded = True
            print("✅ LoRA loaded!")
        except Exception as e:
            print(f"⚠️  LoRA failed: {type(e).__name__}")
            print("   → Continuing without LoRA (4GB VRAM limit)")
    else:
        print(f"⚠️  LoRA file not found: {lora_path}")
    
    # Clear memory again
    gc.collect()
    if device == "cuda":
        torch.cuda.empty_cache()
    
    print("="*60 + "\n")
    return lora_loaded

@app.route('/')
def home():
    gpu_name = torch.cuda.get_device_name(0) if device == "cuda" else "CPU"
    return render_template('index.html', device=device, gpu_name=gpu_name)

@app.route('/enhance-prompt', methods=['POST'])
def enhance_prompt():
    try:
        data = request.json
        user_prompt = data.get('prompt', '')
        
        if not user_prompt:
            return jsonify({'error': 'Prompt trống'}), 400
        
        enhanced = enhance_prompt_with_gemini(user_prompt)
        
        return jsonify({'success': True, 'enhanced': enhanced})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Clear memory before generate
        gc.collect()
        if device == "cuda":
            torch.cuda.empty_cache()
        
        data = request.json
        prompt = data.get('prompt', '')
        steps = int(data.get('steps', 25))  # Giảm từ 30→25 cho 4GB VRAM
        cfg = float(data.get('cfg', 5.0))
        seed = int(data.get('seed', -1))
        width = int(data.get('width', 512))
        height = int(data.get('height', 512))
        
        # Giới hạn resolution cho 4GB VRAM
        max_pixels = 512 * 512  # 262K pixels
        if width * height > max_pixels:
            # Auto-scale down
            scale = (max_pixels / (width * height)) ** 0.5
            width = int(width * scale / 64) * 64  # Round to 64
            height = int(height * scale / 64) * 64
            print(f"⚠️  Resolution scaled down to {width}x{height} (4GB VRAM limit)")
        
        if not prompt:
            return jsonify({'error': 'Prompt trống'}), 400
        
        if seed == -1:
            seed = random.randint(0, 2147483647)
        
        # Simple prompt format (LoRA loaded via diffusers)
        full_prompt = prompt
        negative_prompt = "lowres, blurry, low quality, bad body anatomy, letterbox, deformity, mutilated, malformed, amputee, watermark, signature"
        
        print(f"\n🎨 Generating: {width}x{height}, steps={steps}, seed={seed}")
        print(f"   Prompt: {prompt[:60]}...")
        
        generator = torch.Generator(device=device).manual_seed(seed)
        
        # Generate with error handling
        try:
            image = pipeline(
                prompt=full_prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=steps,
                guidance_scale=cfg,
                width=width,
                height=height,
                generator=generator
            ).images[0]
        except RuntimeError as e:
            if "out of memory" in str(e).lower():
                # Retry with even smaller size for 4GB VRAM
                print("⚠️  VRAM OOM! Retrying with 384x384, 20 steps...")
                gc.collect()
                torch.cuda.empty_cache()
                image = pipeline(
                    prompt=full_prompt,
                    negative_prompt=negative_prompt,
                    num_inference_steps=20,
                    guidance_scale=cfg,
                    width=384,
                    height=384,
                    generator=generator
                ).images[0]
                width, height = 384, 384
            else:
                raise
        
        buffered = BytesIO()
        image.save(buffered, format="PNG", optimize=True)
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # Clear memory after generate
        gc.collect()
        if device == "cuda":
            torch.cuda.empty_cache()
        
        print("✅ Done!\n")
        
        return jsonify({
            'success': True,
            'image': f'data:image/png;base64,{img_str}',
            'seed': seed,
            'prompt_used': full_prompt,
            'actual_size': f'{width}x{height}'
        })
        
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🎨 Kurzgesagt AI - LITE MODE")
    print("="*60)
    print("Tối ưu cho máy RAM thấp (chưa tăng Virtual Memory)")
    print("Default: 512x512, 30 steps")
    print("="*60 + "\n")
    
    lora_status = load_model_once()
    
    print("\n" + "="*60)
    print("🚀 SERVER READY")
    print("="*60)
    print(f"LoRA: {'✅ Active' if lora_status else '⚠️  Not loaded'}")
    print("URL: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=False)
