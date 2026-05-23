# =========================================
# AI SMALL BUSINESS IDEA GENERATOR
# =========================================

from groq import Groq
from dotenv import load_dotenv
import os
import time

# =========================================
# API CONFIGURATION
# =========================================

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# =========================================
# TITLE
# =========================================

print("=" * 60)
print("       AI SMALL BUSINESS IDEA GENERATOR")
print("=" * 60)

# =========================================
# USER INPUT
# =========================================

interest = input("Enter your interest area: ")
budget = input("Enter your budget in ₹: ")
location = input("Enter location type (Village/City/Town): ")

print("\nGenerating business ideas...\n")

# =========================================
# PROMPT
# =========================================

prompt = f"""
You are an expert startup mentor.

Generate 5 practical small business ideas.

Interest Area: {interest}
Budget: ₹{budget}
Location Type: {location}

For each business idea provide:

1. Business Name
2. Problem It Solves
3. Target Audience
4. Estimated Investment
5. Expected Profit
6. Why It Can Succeed

Requirements:
- Beginner friendly
- Practical ideas
- Indian market suitable
- Budget friendly
- Clear formatting
"""

# =========================================
# AI GENERATION (GROQ)
# =========================================

try:

    time.sleep(1)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a startup business expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    output_text = response.choices[0].message.content

    # =========================================
    # OUTPUT
    # =========================================

    print("=" * 60)
    print("            GENERATED BUSINESS IDEAS")
    print("=" * 60)
    print()

    print(output_text)

    # =========================================
    # SAVE OUTPUT
    # =========================================

    with open("business_ideas.txt", "w", encoding="utf-8") as file:
        file.write(output_text)

    print("\nResults saved in business_ideas.txt")

    print("\n" + "=" * 60)
    print("IDEAS GENERATED SUCCESSFULLY ✅")
    print("Think Smart • Start Small • Grow Big 🚀")
    print("=" * 60)

# =========================================
# ERROR HANDLING
# =========================================

except Exception as e:

    print("\n❌ ERROR OCCURRED")
    print("Details:", e)

    print("\nTry These Fixes:")
    print("1. Check GROQ_API_KEY in .env file")
    print("2. Internet connection issue")
    print("3. Groq rate limit exceeded")
    print("4. Wrong model name")