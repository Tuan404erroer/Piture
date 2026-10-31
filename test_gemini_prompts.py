"""Test Gemini creative prompt generation"""
import google.generativeai as genai

# Load API key
with open('.streamlit/secrets.toml', 'r') as f:
    api_key = f.read().split('=')[1].strip().strip('"')
genai.configure(api_key=api_key)

gemini_model = genai.GenerativeModel('gemini-1.5-flash')

def test_prompt(user_input):
    system_prompt = f"""You are a creative storyteller for Kurzgesagt-style educational videos. Your job is to CREATE a detailed, vivid scene description.

USER IDEA: "{user_input}"

YOUR TASK: Expand this into a FULL SCENE with rich visual details, following these examples:

EXAMPLE 1:
User: "ancient civilization"
You create: civilization, people, building, market, mayan pyramid, sky, day, vector art, Kurzgesagt, sharp focus, HDR, 8k, gigapixel, masterpiece

EXAMPLE 2:
User: "night tribal scene"
You create: starry, fire, torch, aborigines, night, moon, people, tribe, vector art, Kurzgesagt, sharp focus, HDR, 8k, gigapixel, masterpiece

EXAMPLE 3:
User: "alien planet"
You create: people, sun, sea, mountain, yellow sky, two sun, red sea, astronaut, vector art, Kurzgesagt, sharp focus, HDR, 8k, gigapixel, masterpiece

EXAMPLE 4:
User: "ocean life"
You create: ocean, sea, fish, coral, water, aquatic, blue background, jellyfish, underwater, sunlight rays, vector art, Kurzgesagt, sharp focus, HDR, 8k, masterpiece

CREATIVE RULES:
1. **Be specific**: Add concrete objects (pyramid, torch, astronaut, coral)
2. **Set atmosphere**: Include time (day/night), weather, lighting (starry, sunset, fire)
3. **Add life**: Include people, animals, or characters when relevant
4. **Rich details**: Colors (yellow sky, red sea), environment elements
5. **Tell a story**: Create a scene that feels like a Kurzgesagt video frame

REQUIRED FORMAT:
[scene elements, separated by commas], vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))

OUTPUT: Return ONLY the comma-separated prompt. No explanations, no quotes, no extra text."""

    response = gemini_model.generate_content(system_prompt)
    enhanced = response.text.strip()
    enhanced = enhanced.replace('*', '').replace('`', '').replace('"', '').strip()
    enhanced = enhanced.replace('\n', ' ').replace('  ', ' ')
    
    # Ensure proper ending
    required_ending = "vector art, Kurzgesagt, sharp focus, (HDR), (8k), (gigapixel), ((masterpiece))"
    for term in ["vector art", "kurzgesagt", "sharp focus", "HDR", "8k", "gigapixel", "masterpiece"]:
        enhanced = enhanced.replace(f", {term}", "").replace(term, "")
    enhanced = enhanced.strip().rstrip(',').strip()
    enhanced = f"{enhanced}, {required_ending}"
    
    return enhanced

print("=" * 80)
print("GEMINI CREATIVE PROMPT TEST")
print("=" * 80)

test_inputs = [
    "ocean scene",
    "ancient civilization", 
    "space exploration",
    "forest animals",
    "underwater world"
]

for user_input in test_inputs:
    print(f"\n{'='*80}")
    print(f"INPUT: {user_input}")
    print(f"{'='*80}")
    result = test_prompt(user_input)
    print(f"\nOUTPUT:\n{result}")
    print()

print("=" * 80)
print("Test complete!")
print("=" * 80)
