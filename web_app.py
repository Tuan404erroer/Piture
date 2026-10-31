import sys
import io
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from flask import Flask, render_template, request, jsonify
import torch
from diffusers.pipelines import StableDiffusionPipeline
from diffusers.schedulers import DPMSolverMultistepScheduler
import random
from io import BytesIO
import base64
import google.generativeai as genai
import gc  # Garbage collector để giải phóng RAM

app = Flask(__name__)

# Load API key
with open('.streamlit/secrets.toml', 'r') as f:
    api_key = f.read().split('=')[1].strip().strip('"')
genai.configure(api_key=api_key)

gemini_model = genai.GenerativeModel('gemini-3.1-flash-lite')

pipeline = None
device = None
current_model = None  # Track which model is loaded

def ensure_ruan_jia_attribution(prompt):
    """Add Ruan Jia attribution if Gemini missed it."""
    if "by ruan jia" in prompt.lower():
        return prompt

    attribution = "by Ruan Jia"
    line_markers = ["\nlineless", "\nby kurzgesagt", "\nvector art"]
    for marker in line_markers:
        if marker in prompt:
            return prompt.replace(marker, f"\n{attribution}{marker}", 1)

    inline_markers = [", lineless", ", by kurzgesagt", ", vector art"]
    for marker in inline_markers:
        if marker in prompt:
            return prompt.replace(marker, f", {attribution}{marker}", 1)

    return f"{prompt.rstrip()}\n\n{attribution}"

def enhance_prompt_with_gemini(user_prompt):
    """Gemini tạo prompt với LAYERS structure: Foreground → Midground → Background → Sky"""
    
    system_prompt = f"""You are a visual scene designer who thinks in LAYERS and DEPTH.

USER INPUT: "{user_prompt}"

YOUR TASK: Transform the user's idea into a layered scene with depth and perspective.

OUTPUT FORMAT (EXACT STRUCTURE - include the <lora> tag at the start):

<lora:S1-Kurzgesagt_DreamLike-000008:1>

(Foreground)
[3-5 items in front, closest to viewer: detailed objects, main subjects, foreground elements]

(Midground)
[5-8 items in middle distance: secondary elements, environment features, context]

(Background)
[4-6 items far away: distant objects, horizon, far landscape]

(Sky / Lighting)
[3-5 items: sky elements, weather, lighting atmosphere, time of day]

by [Artist 1]
lineless
by kurzgesagt
vector art
kurzgesagt
flat colors
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))

ARTIST SELECTION (choose 1-2 that fit the scene):
- Nature/Landscape: Ruan Jia, Hiroshi Yoshida, Hasui Kawase, Thomas Kinkade
- Sci-fi/Tech: Simon Stålenhag, Syd Mead, Ralph McQuarrie
- Fantasy/Magic: James Gurney, Greg Rutkowski, Atey Ghailan
- Modern/Digital: Makoto Shinkai, Ismail Inceoglu, Alayna Lemmer

THINKING PROCESS:

1. UNDERSTAND USER'S IDEA: "{user_prompt}"
   - What is the main subject?
   - What is its SCALE (small vs large)?
   - What environment/setting?
   - What mood/atmosphere?

2. DETERMINE PERSPECTIVE BY SCALE:

   LARGE SUBJECTS (place closer):
   - Massive: galaxies, planets, nebulas, solar systems
   - Very large: mountains, buildings, cities, forests, oceans
   - Big structures: skyscrapers, castles, temples, bridges
   - Large creatures: whales, elephants, dragons
   → Place in FOREGROUND/MIDGROUND (close to camera to show scale and details)
   → Background: cosmic space, distant landscape, atmosphere

   SMALL SUBJECTS (place farther):
   - Microscopic: atoms, molecules, cells, DNA, bacteria
   - Tiny: insects, small flowers, particles
   - Small objects: pebbles, leaves, small fish
   - Small creatures: birds flying, butterflies
   → Place in MIDGROUND/BACKGROUND (farther to maintain perspective)
   → Foreground: environment context, viewing frame
   → Sky: atmospheric elements

3. BUILD LAYERS:
   
   FOREGROUND (closest to camera):
   - For LARGE subjects: The main subject itself + massive details
   - For SMALL subjects: Environment context, ground, nearby larger objects
   
   MIDGROUND (middle distance):
   - For LARGE subjects: Secondary details, environmental context
   - For SMALL subjects: The main subject + surrounding environment
   
   BACKGROUND (far):
   - For LARGE subjects: Distant cosmic/atmospheric context
   - For SMALL subjects: Blurred far elements, depth atmosphere
   
   SKY / LIGHTING:
   - Atmospheric elements, lighting, weather, cosmic effects

EXAMPLES:

Input: "forest sunset"
Output:
<lora:S1-Kurzgesagt_DreamLike-000008:1>

(Foreground)
wildflowers blooming, moss-covered rocks, fallen log, mushrooms, ferns

(Midground)
dense pine trees, oak trunks, deer grazing, small stream, wooden bridge, forest floor

(Background)
distant mountains, mountain peaks, valley, far treeline, misty horizon

(Sky / Lighting)
golden sunset, warm orange glow, dramatic clouds, light rays filtering through trees, dusk atmosphere

by Ruan Jia
lineless
by kurzgesagt
vector art
kurzgesagt
flat colors
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))

---

Input: "ocean underwater"
Output:
<lora:S1-Kurzgesagt_DreamLike-000008:1>

(Foreground)
colorful coral, clownfish, sea anemone, starfish, shells on sand

(Midground)
coral reef formations, sea turtle swimming, jellyfish floating, schools of fish, seaweed swaying, underwater rocks

(Background)
deep blue water, distant reef, ocean depth, water gradient, sandy ocean floor

(Sky / Lighting)
sunlight rays penetrating water, god rays, water surface ripples above, turquoise light, clear visibility

by Ruan Jia
lineless
by kurzgesagt
vector art
kurzgesagt
flat colors
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))

CRITICAL RULES:
1. ALWAYS START with: <lora:S1-Kurzgesagt_DreamLike-000008:1>
2. Then add blank line
3. START by analyzing user input: "{user_prompt}"
4. THINK in layers: front → middle → back → sky
5. 3-5 items in Foreground, 5-8 in Midground, 4-6 in Background, 3-5 in Sky
6. Select 1-2 artists that fit the mood
7. ALWAYS include artist attribution AFTER Sky/Lighting section:
   by Ruan Jia (or another fitting artist)
   lineless
   by kurzgesagt
   vector art
   kurzgesagt
   flat colors
   sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))
   
8. Artist MUST appear between Sky/Lighting and lineless

OUTPUT: The layered prompt following EXACT format above, starting with <lora> tag."""

    try:
        # HIGH randomness để mỗi lần khác nhau
        import random
        generation_config = {
            'temperature': 1.5,  # Very high creativity
            'top_p': 0.98,
            'top_k': 100,
            'max_output_tokens': 2048,
            'candidate_count': 1,
        }
        
        # Add timestamp/random seed to make it more unique
        timestamp_hint = f"\n\n[Generation #{random.randint(1000, 9999)} - create a COMPLETELY DIFFERENT scene]"
        
        response = gemini_model.generate_content(
            system_prompt + timestamp_hint,
            generation_config=generation_config
        )
        enhanced = response.text.strip()
        
        # Clean but preserve line breaks
        enhanced = enhanced.replace('*', '').replace('`', '').replace('"', '')
        
        # Ensure <lora> tag is at the start
        if not enhanced.startswith('<lora:'):
            enhanced = f"<lora:S1-Kurzgesagt_DreamLike-000008:1>\n\n{enhanced}"
        
        # CRITICAL: Ensure artist name is ALWAYS present
        has_artist = False
        for artist_marker in ["by Ruan Jia", "by Hiroshi", "by Atey", "by Simon", "by James", "by Makoto"]:
            if artist_marker in enhanced:
                has_artist = True
                break
        
        if not has_artist:
            # Force add artist name at correct position
            print("⚠️  No artist found, adding 'by Ruan Jia'")
            
            # Find best insertion point
            if "(Sky / Lighting)" in enhanced:
                # Split at Sky/Lighting section end and insert artist
                lines = enhanced.split('\n')
                new_lines = []
                sky_section_ended = False
                
                for i, line in enumerate(lines):
                    new_lines.append(line)
                    # After Sky/Lighting section ends (empty line or next section)
                    if sky_section_ended and not line.strip() and i + 1 < len(lines):
                        if not lines[i + 1].startswith('by '):
                            new_lines.append('')
                            new_lines.append('by Ruan Jia')
                            sky_section_ended = False
                    elif "(Sky / Lighting)" in line:
                        # Mark that we're in sky section
                        sky_section_ended = False
                    elif line.strip() and not line.startswith('(') and "(Sky / Lighting)" in '\n'.join(lines[:i]):
                        # First non-empty line after sky content
                        if not sky_section_ended and not line.startswith('by '):
                            sky_section_ended = True
                
                enhanced = '\n'.join(new_lines)
            
            # Fallback: insert before "lineless" or "vector art"
            if "by " not in enhanced:
                if "lineless" in enhanced:
                    enhanced = enhanced.replace("\nlineless", "\n\nby Ruan Jia\nlineless")
                elif "vector art" in enhanced:
                    enhanced = enhanced.replace("\nvector art", "\n\nby Ruan Jia\nvector art")
                else:
                    enhanced = enhanced + "\n\nby Ruan Jia"
        
        # Ensure format structure exists
        if "(Foreground)" not in enhanced:
            # Fallback structure
            enhanced = f"""<lora:S1-Kurzgesagt_DreamLike-000008:1>

(Foreground)
{user_prompt}, detailed elements, close-up objects

(Midground)
environment context, middle distance features, landscape elements

(Background)
distant scenery, horizon, far structures, atmospheric depth

(Sky / Lighting)
sky condition, lighting atmosphere, time of day effects

by Ruan Jia
lineless
by kurzgesagt
vector art
kurzgesagt
flat colors
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))"""
        
        enhanced = ensure_ruan_jia_attribution(enhanced)
        return enhanced.strip()
        
    except Exception as e:
        print(f"Gemini error: {e}")
        # Fallback with structure
        return f"""<lora:S1-Kurzgesagt_DreamLike-000008:1>

(Foreground)
{user_prompt}, main subject, detailed foreground elements

(Midground)
environment features, contextual elements, mid-distance objects

(Background)
distant landscape, horizon, far scenery, depth

(Sky / Lighting)
atmospheric lighting, sky elements, mood

by Ruan Jia
lineless
by kurzgesagt
vector art
kurzgesagt
flat colors
sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))"""

def load_model_once():
    global pipeline, device, current_model
    
    # If already loaded, skip
    if current_model == "dreamlike" and pipeline is not None:
        print(f"✅ Model already loaded, skipping...")
        return True
    
    print(f"🔄 Loading Dreamlike Diffusion...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Giải phóng RAM trước khi load
    gc.collect()
    if device == "cuda":
        torch.cuda.empty_cache()
    
    model_id = "dreamlike-art/dreamlike-diffusion-1.0"
    print(f"📦 Model: Dreamlike Diffusion 1.0 (Vector Art)")
    
    # Load from HuggingFace
    print(f"🌐 Loading from HuggingFace: {model_id}")
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None,
        low_cpu_mem_usage=True
    )
    
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
        pipeline.scheduler.config,
        algorithm_type="dpmsolver++",
        use_karras_sigmas=True
    )
    
    pipeline = pipeline.to(device)
    print("✅ Base model loaded")
    
    if device == "cuda":
        # Tối ưu VRAM/RAM
        pipeline.enable_attention_slicing()
        pipeline.enable_vae_slicing()
        pipeline.enable_model_cpu_offload()  # Offload một phần sang CPU
        print("✅ Memory optimizations enabled")
    
    # Load Kurzgesagt LoRA
    print("\n" + "=" * 60)
    print("🔄 Loading Kurzgesagt LoRA...")
    print("=" * 60)
    lora_loaded = False
    
    try:
        pipeline.load_lora_weights("models", weight_name="Kurzgesagt_v1.safetensors")
        lora_loaded = True
        print("✅ LoRA LOADED SUCCESSFULLY!")
        print("   Images will have authentic Kurzgesagt style")
    except Exception as e:
        print(f"❌ LoRA LOAD FAILED: {type(e).__name__}")
        print(f"   Error: {str(e)[:200]}")
        print("\n⚠️  RUNNING WITHOUT LORA!")
        print("   Images will be generic vector art, NOT Kurzgesagt style")
    
    print("=" * 60 + "\n")
    
    print(f"✅ Pipeline ready on {device}")
    if device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    
    # Update current model tracker
    current_model = "dreamlike"
    
    return lora_loaded

@app.route('/')
def home():
    gpu_name = torch.cuda.get_device_name(0) if device == "cuda" else "CPU"
    return render_template('index.html', device=device, gpu_name=gpu_name, current_model="dreamlike")

@app.route('/enhance-prompt', methods=['POST'])
def enhance_prompt():
    try:
        data = request.json
        user_prompt = data.get('prompt', '')
        
        if not user_prompt:
            return jsonify({'error': 'Prompt trống'}), 400
        
        print(f"\n🤖 Gemini enhancing: {user_prompt}")
        
        enhanced = enhance_prompt_with_gemini(user_prompt)
        negative = generate_negative_prompt(user_prompt)
        
        print(f"✅ Enhanced prompt")
        print(f"✅ Generated negative prompt")
        
        return jsonify({
            'success': True, 
            'enhanced': enhanced,
            'negative': negative,
            'original': user_prompt
        })
    except Exception as e:
        print(f"❌ Enhance error: {e}")
        return jsonify({'error': str(e)}), 500


def generate_negative_prompt(user_prompt):
    """Gemini tạo negative prompt phù hợp với ý tưởng user"""
    
    system_prompt = f"""You are a Stable Diffusion negative prompt expert.

USER IDEA: "{user_prompt}"

BASE NEGATIVE PROMPTS (choose and combine):

Option 1 (General quality):
lowres, blurry, error, jpeg artifacts, low quality, normal quality, worst quality, messy, letterbox, monochrome, sketch

Option 2 (Anatomy/deformity):
lowres, blurry, low quality, bad body anatomy, letterbox, deformity, mutilated, malformed, amputee, watermark, signature

Option 3 (Technical issues):
blurry, out of focus, low resolution, pixelated, compression artifacts, noise, grainy, watermark, text, logo

Option 4 (Style issues):
sketch, draft, unfinished, messy, chaotic, cluttered, poorly drawn, amateur, low detail

TASK: Select and combine relevant negative terms based on user's idea.

RULES:
1. Always include: lowres, blurry, low quality
2. If people/animals: add anatomy terms (bad body anatomy, deformity, mutilated, malformed)
3. If landscape/nature: add (messy, cluttered, chaotic)
4. Always end with: watermark, signature

EXAMPLES:

Input: "cat"
Output: lowres, blurry, low quality, bad body anatomy, deformity, mutilated, malformed, amputee, messy, watermark, signature

Input: "ocean"
Output: lowres, blurry, low quality, messy, cluttered, chaotic, murky, dirty, watermark, signature

Input: "city"
Output: lowres, blurry, low quality, messy, cluttered, chaotic, poorly drawn, watermark, signature

OUTPUT: Return only comma-separated negative prompt."""

    try:
        response = gemini_model.generate_content(system_prompt)
        negative = response.text.strip()
        negative = negative.replace('*', '').replace('`', '').replace('"', '').strip()
        
        # Ensure basic terms
        if "lowres" not in negative:
            negative = f"lowres, blurry, low quality, {negative}"
        if "watermark" not in negative and "signature" not in negative:
            negative = f"{negative}, watermark, signature"
            
        return negative.strip()
        
    except Exception as e:
        print(f"Negative prompt error: {e}")
        # Default fallback
        return "lowres, blurry, low quality, bad body anatomy, letterbox, deformity, mutilated, malformed, amputee, watermark, signature"



@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        negative_prompt = data.get('negative_prompt', '')
        steps = int(data.get('steps', 50))
        cfg = float(data.get('cfg', 5.0))
        seed = int(data.get('seed', -1))
        width = int(data.get('width', 512))
        height = int(data.get('height', 768))
        
        # Ensure model is loaded
        if pipeline is None:
            load_model_once()
        
        if not prompt:
            return jsonify({'error': 'Prompt trống'}), 400
        
        if seed == -1:
            seed = random.randint(0, 2147483647)
        
        # Prompt đã có <lora> tag và format đầy đủ từ Gemini
        # Chỉ cần dùng trực tiếp
        full_prompt = prompt
        
        # Use custom negative or default
        if not negative_prompt:
            negative_prompt = "lowres, blurry, low quality, bad body anatomy, letterbox, deformity, mutilated, malformed, amputee, watermark, signature"
        
        print(f"\n{'='*60}")
        print(f"🎨 Generating Image")
        print(f"{'='*60}")
        print(f"Prompt: {full_prompt[:100]}...")
        print(f"Negative: {negative_prompt[:80]}...")
        print(f"Steps: {steps} | CFG: {cfg} | Seed: {seed}")
        print(f"Size: {width}x{height}")
        print(f"{'='*60}\n")
        
        generator = torch.Generator(device=device).manual_seed(seed)
        
        image = pipeline(
            prompt=full_prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            guidance_scale=cfg,
            width=width,
            height=height,
            generator=generator
        ).images[0]
        
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        print("✅ Image generated successfully!\n")
        
        return jsonify({
            'success': True,
            'image': f'data:image/png;base64,{img_str}',
            'seed': seed,
            'prompt_used': full_prompt,
            'negative_used': negative_prompt
        })
        
    except Exception as e:
        print(f"❌ Generation error: {e}\n")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    lora_status = load_model_once()
    
    print("\n" + "="*60)
    print("🎨 Kurzgesagt AI + Gemini")
    print("="*60)
    if lora_status:
        print("✅ LoRA Model: ACTIVE (Authentic Kurzgesagt style)")
    else:
        print("⚠️  LoRA Model: NOT LOADED (Generic style only)")
    print("="*60)
    print("Server: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
