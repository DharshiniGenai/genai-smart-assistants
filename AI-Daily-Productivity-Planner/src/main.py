# =========================================
# AI DAILY PRODUCTIVITY PLANNER (GROQ VERSION)
# =========================================

from groq import Groq
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

# Check API key
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize Groq client
client = Groq(api_key=api_key)

# =========================================
# TITLE
# =========================================

print("=" * 60)
print("        AI DAILY PRODUCTIVITY PLANNER")
print("=" * 60)

# =========================================
# USER INPUT
# =========================================

wake_up = input("Enter your wake-up time (e.g., 6:00 AM): ")
work_hours = input("Enter your work/study hours per day: ")
goals = input("Enter your daily goals (comma separated): ")

print("\nGenerating your optimized schedule...\n")

# =========================================
# PROMPT ENGINEERING
# =========================================

prompt = f"""
You are an expert AI productivity coach.

Create a structured DAILY PRODUCTIVITY PLAN.

User Details:
- Wake-up time: {wake_up}
- Work hours: {work_hours}
- Goals: {goals}

Output format:
1. Morning Routine
2. Work Schedule (time blocks)
3. Break Schedule
4. Evening Routine
5. Night Routine
6. Productivity Tips (5-8 points)

Rules:
- Must be realistic
- Must include time blocks
- Must balance work + health + rest
- Must be beginner friendly
- Must be practical for students or employees
"""

# =========================================
# AI CALL (GROQ FIXED)
# =========================================

try:
    time.sleep(1)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert productivity coach."},
            {"role": "user", "content": prompt}
        ]
    )

    # =========================================
    # OUTPUT
    # =========================================

    print("=" * 60)
    print("        YOUR DAILY PRODUCTIVITY PLAN")
    print("=" * 60)
    print()

    print(response.choices[0].message.content)

    print("\n" + "=" * 60)
    print("PLAN GENERATED SUCCESSFULLY ✅")
    print("Stay consistent • Stay disciplined • Improve daily 🚀")
    print("=" * 60)

except Exception as e:
    print("\n❌ ERROR OCCURRED")
    print("Details:", e)

    print("\nPossible Fixes:")
    print("1. Check GROQ_API_KEY in .env")
    print("2. Check internet connection")
    print("3. Use correct model: llama-3.1-70b-versatile")
    print("4. Install groq package properly")