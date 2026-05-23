# =========================================
# Assignment 1: AI Personal Fitness Coach
# Groq API + LLaMA Version
# =========================================

from groq import Groq
from dotenv import load_dotenv
import os

# =========================================
# STEP 1: LOAD API KEY
# =========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

print("=" * 60)
print("          AI PERSONAL FITNESS COACH")
print("=" * 60)

# =========================================
# STEP 2: USER INPUT
# =========================================

name = input("Enter your name: ")
age = input("Enter your age: ")
weight = input("Enter your weight (kg): ")
goal = input("Enter your fitness goal (Weight Loss / Weight Gain / Muscle Gain): ")
time_available = input("Enter workout time available per day (minutes): ")
budget = input("Enter your daily food budget in ₹: ")
gym_access = input("Gym Access? (Yes/No): ")
lifestyle = input("Enter your lifestyle/profession: ")

print("\nGenerating your personalized 7-day fitness plan...\n")

# =========================================
# STEP 3: PROMPT
# =========================================

prompt = f"""
You are a professional fitness coach and nutrition expert.

Create a beginner-friendly 7-day fitness and diet plan.

USER DETAILS:
Name: {name}
Age: {age}
Weight: {weight} kg
Goal: {goal}
Workout Time: {time_available} minutes
Daily Food Budget: ₹{budget}
Gym Access: {gym_access}
Lifestyle: {lifestyle}

RULES:
1. Keep workouts beginner friendly
2. Keep meals affordable within budget
3. Suggest Indian foods
4. Include breakfast, lunch, dinner
5. Include calories
6. Include hydration tips
7. Include daily motivation
8. Include sleep recommendation

FORMAT:

Day 1:
Workout:
Diet:
Calories:
Motivation:

Continue until Day 7.
"""

# =========================================
# STEP 4: GENERATE RESPONSE
# =========================================

try:

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=4000
    )

    result = response.choices[0].message.content

    # =========================================
    # OUTPUT
    # =========================================

    print("=" * 60)
    print("        YOUR 7-DAY FITNESS PLAN")
    print("=" * 60)
    print()

    print(result)

    print("\n" + "=" * 60)
    print("PLAN GENERATED SUCCESSFULLY ✅")
    print("Stay consistent and trust the process 💪")
    print("=" * 60)

# =========================================
# ERROR HANDLING
# =========================================

except Exception as e:

    print("\n❌ ERROR OCCURRED")
    print("Details:", e)

    print("\nPossible Fixes:")
    print("1. Check internet connection")
    print("2. Verify GROQ API key")
    print("3. Ensure required packages are installed")
    print("4. Check if Groq API service is available")
    print("5. Retry after a few seconds")