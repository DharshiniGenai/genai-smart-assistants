# =========================================
# AI RESTAURANT RECOMMENDER
# =========================================

from groq import Groq
from dotenv import load_dotenv
import os
import time

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# API CONFIGURATION
# =========================================

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# =========================================
# TITLE
# =========================================

print("=" * 60)
print("        AI RESTAURANT RECOMMENDER")
print("=" * 60)

# =========================================
# USER INPUT
# =========================================

food_pref = input("Enter food preference (veg/non-veg/vegan/etc): ")
budget = input("Enter your budget per meal (₹): ")
cuisine = input("Enter cuisine type (Indian/Chinese/Italian/etc): ")
health_goal = input("Enter health goal (weight loss/muscle gain/normal): ")

print("\nGenerating meal recommendations...\n")

# =========================================
# PROMPT ENGINEERING
# =========================================

prompt = f"""
You are an expert nutritionist and food recommendation AI.

Suggest 5 meal ideas based on user preferences.

User Details:
- Food Preference: {food_pref}
- Budget per meal: ₹{budget}
- Cuisine: {cuisine}
- Health Goal: {health_goal}

For each meal provide:

1. Meal Name
2. Ingredients (simple list)
3. Estimated Cost (₹)
4. Calories (approx)
5. Why it is suitable

Rules:
- Budget friendly (important)
- Healthy and practical
- Indian market suitable foods
- Easy to cook or order
- Clear structured format
"""

# =========================================
# AI CALL
# =========================================

try:

    time.sleep(1)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=2500
    )

    result = response.choices[0].message.content

    # =========================================
    # OUTPUT
    # =========================================

    print("=" * 60)
    print("        YOUR MEAL RECOMMENDATIONS")
    print("=" * 60)
    print()

    print(result)

    print("\n" + "=" * 60)
    print("MEALS GENERATED SUCCESSFULLY ✅")
    print("Eat healthy • Stay fit • Stay strong 💪")
    print("=" * 60)

# =========================================
# ERROR HANDLING
# =========================================

except Exception as e:

    print("\n❌ ERROR OCCURRED")
    print("Details:", e)

    print("\nPossible Fixes:")
    print("1. Check GROQ API key")
    print("2. Check internet connection")
    print("3. Retry after some time (rate limit)")
    print("4. Verify model name")