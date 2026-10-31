"""Test Gemini tạo prompts chi tiết với depth và layers"""
import google.generativeai as genai

# Load API key
with open('.streamlit/secrets.toml', 'r') as f:
    api_key = f.read().split('=')[1].strip().strip('"')
genai.configure(api_key=api_key)

gemini_model = genai.GenerativeModel('gemini-1.5-flash')

test_inputs = [
    "forest mountains river wildlife sunset",
    "ocean underwater scene",
    "city skyline at night",
    "desert landscape",
    "space station"
]

print("="*80)
print("GEMINI DETAILED PROMPT TEST - Depth & Layers")
print("="*80)

for user_input in test_inputs:
    print(f"\n{'='*80}")
    print(f"INPUT: {user_input}")
    print(f"{'='*80}")
    
    system_prompt = f"""You are a Kurzgesagt scene designer. Create DETAILED, LAYERED prompts with depth and multiple perspectives.

USER IDEA: "{user_input}"

RULES FOR DETAILED SCENES:

1. **DEPTH LAYERS** (foreground → midground → background):
   - Foreground: Close objects (rocks, plants, animals)
   - Midground: Main subjects (people, buildings, vehicles)
   - Background: Distant elements (mountains, sky, horizon)

2. **MULTIPLE ANGLES/PERSPECTIVES**:
   - Include elements from different heights (ground level, aerial view, eye-level)
   - Add depth cues (things behind, things in front, overlap)

3. **RICH DETAILS**:
   - Specific objects: not just "tree" but "tall pine trees, small bushes, moss-covered rocks"
   - Environment: weather, lighting, time of day, atmosphere
   - Colors: specific color descriptions (golden sunset, deep blue water, emerald forest)
   - Life/motion: birds flying, water flowing, wind effects, people moving

4. **COMPOSITION**:
   - Wide shot elements: landscape, horizon, sky
   - Close details: textures, small creatures, foreground items
   - Multiple focal points across the scene

FORMAT: [foreground details], [midground elements], [background layers], [atmosphere/lighting], vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))

Return ONLY the detailed comma-separated prompt."""

    response = gemini_model.generate_content(system_prompt)
    enhanced = response.text.strip().replace('*', '').replace('`', '').replace('"', '')
    
    print(f"\nOUTPUT:")
    print(enhanced)
    print()

print("="*80)
print("Test complete!")
print("="*80)
