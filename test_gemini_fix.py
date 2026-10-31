"""Test Gemini với requirement 30-50 elements"""
import google.generativeai as genai

# Load API key
with open('.streamlit/secrets.toml', 'r') as f:
    api_key = f.read().split('=')[1].strip().strip('"')
genai.configure(api_key=api_key)

gemini_model = genai.GenerativeModel('gemini-1.5-flash')

user_input = "bird tree"

system_prompt = f"""You are a Kurzgesagt master scene designer. 

USER INPUT: "{user_input}"

⚠️ CRITICAL: Your prompt MUST contain 30-50 ELEMENTS minimum!

MANDATORY STRUCTURE (fill ALL sections):

1. FOREGROUND (8-12 elements):
   - Specific plants, ground items, small creatures, textures

2. MIDGROUND (10-15 elements):
   - Main subjects with DETAILS
   - Trees (specify species)
   - Animals with actions

3. BACKGROUND (8-12 elements):
   - Distant landscape layers
   - Sky details
   - Atmospheric effects

4. LIGHTING & ATMOSPHERE (5-8 elements):
   - Time, light effects, weather, mood

5. LIFE & MOTION (5-8 elements):
   - Birds with species
   - Movement details

EXAMPLE (50+ elements):

Input: "bird tree"
BAD (11 elements): bird, tree, sky, clouds, nature, landscape ❌

GOOD (50+ elements): small blue jay with detailed crest feathers perched on thick oak branch, textured bark with moss patches, acorns hanging, autumn leaves in orange and gold, small twigs, lichen growth, wildflowers at tree base including daisies and buttercups, clover patches, smooth river stones, fallen acorns on grass, tiny mushrooms growing, butterfly landing on flower, ladybug on leaf, spider web glistening, tall oak tree with spreading branches, neighboring maple tree with red leaves, dense foliage canopy, winding dirt path below, small wooden fence with weathered posts, distant evergreen forest, rolling hills with varying shades of green, farmhouse with red roof in distance, smoke from chimney, mountain range on horizon, layered clouds at different heights, blue sky with wispy cirrus clouds, cumulus clouds casting shadows, golden afternoon sunlight streaming through leaves, dappled shadows on ground, warm glow on bark, sun rays visible through branches, gentle breeze rustling leaves, grass blades swaying, other birds flying in background including sparrows and finches, dragonfly hovering, bees buzzing around flowers, peaceful atmosphere, serene mood, rich colors, depth of field, atmospheric perspective ✅

RETURN: Only comma-separated prompt with 30-50 elements."""

print("="*80)
print(f"TEST: {user_input}")
print("="*80)

response = gemini_model.generate_content(system_prompt)
enhanced = response.text.strip().replace('*', '').replace('`', '').replace('"', '')

# Count
elements = len([e.strip() for e in enhanced.split(',') if e.strip()])

print(f"\nGENERATED PROMPT ({elements} elements):")
print("-"*80)
print(enhanced)
print("-"*80)

if elements >= 30:
    print(f"\n✅ SUCCESS: {elements} elements (target: 30-50)")
else:
    print(f"\n❌ FAILED: Only {elements} elements (need 30+)")

print("="*80)
