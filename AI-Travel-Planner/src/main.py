# =========================================
# AI TRAVEL PLANNER (GROQ VERSION)
# =========================================

from groq import Groq
from dotenv import load_dotenv
import os

# =========================================
# API CONFIGURATION
# =========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

# =========================================
# TITLE
# =========================================

print("=" * 50)
print("           AI TRAVEL PLANNER")
print("=" * 50)

# =========================================
# USER INPUT
# =========================================

city = input("Enter destination city: ")
budget = input("Enter your budget in ₹: ")
interests = input("Enter your interests (food, nature, shopping, adventure, etc): ")

print("\nGenerating your 3-day travel itinerary...\n")

# =========================================
# PROMPT
# =========================================

prompt = f"""
You are an expert AI Travel Planner.

Create a detailed and beginner-friendly 3-day travel itinerary.

Destination City: {city}
Budget: ₹{budget}
Interests: {interests}

Requirements:
1. Day-wise itinerary
2. Morning, afternoon, and evening schedule
3. Places to visit
4. Estimated daily cost
5. Food suggestions
6. Travel tips
7. Budget-friendly recommendations
8. Simple and clear format
"""

# =========================================
# AI RESPONSE (GROQ)
# =========================================

try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert travel planner."},
            {"role": "user", "content": prompt}
        ]
    )

    # =========================================
    # OUTPUT
    # =========================================

    print("=" * 50)
    print("         YOUR 3-DAY TRAVEL PLAN")
    print("=" * 50)
    print()

    print(response.choices[0].message.content)

    print("\n" + "=" * 50)
    print("PLAN GENERATED SUCCESSFULLY ✅")
    print("Have a safe journey ✈️")
    print("=" * 50)

# =========================================
# ERROR HANDLING
# =========================================

except Exception as e:
    print("\n❌ Error Occurred")
    print("Details:", e)

    print("\nPossible Reasons:")
    print("1. Invalid GROQ API key")
    print("2. Internet connection issue")
    print("3. API rate limit exceeded")
    print("4. Wrong model name (use llama-3.1-70b-versatile)")