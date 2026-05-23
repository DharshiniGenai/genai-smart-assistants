GenAI Smart Assistants Collection 🤖🚀

🚀 Built as a collection of real-world AI applications using Groq API + LLaMA models

An intelligent collection of AI-powered assistant applications developed using Python, Groq API, and LLaMA models to solve real-world problems like productivity planning, travel itinerary generation, restaurant recommendations, fitness coaching, and startup idea generation.

This repository contains multiple beginner-friendly AI projects that demonstrate how Generative AI can be integrated into practical applications using prompt engineering and API-based AI systems.

📖 Project Overview

The GenAI Smart Assistants Collection is a multi-project AI repository designed to showcase practical applications of Generative AI using Python and Groq API.

Each project focuses on solving a different real-world problem through AI-generated recommendations, planning systems, and personalized suggestions.

The collection includes:

AI Travel Planner ✈️
AI Daily Productivity Planner 📅
AI Restaurant Recommender 🍽️
AI Personal Fitness Coach 🏋️
AI Small Business Idea Generator 💼

These applications use the Groq API with LLaMA models to generate intelligent, structured, realistic, and beginner-friendly outputs.

This repository is ideal for:

Students learning Generative AI
Beginners exploring AI projects
Python developers learning API integration
Portfolio building
AI application development practice
✨ Included AI Projects
1. AI Travel Planner ✈️🌍

Generates personalized 3-day travel itineraries including:

Tourist attractions
Food recommendations
Budget planning
Travel tips
Daily schedules
Features
Personalized travel plans
Budget-friendly itinerary generation
Interest-based recommendations
Day-wise planning
Travel safety tips
2. AI Daily Productivity Planner 📅⚡

Creates personalized productivity schedules based on:

Wake-up time
Study/work hours
Daily goals
Features
Time-blocked schedules
Morning and night routines
Productivity tips
Balanced work-rest planning
Beginner-friendly planning system
3. AI Restaurant Recommender 🍽️🤖

Suggests personalized healthy meal recommendations based on:

Food preference
Budget
Cuisine type
Health goals
Features
Healthy meal suggestions
Calorie estimation
Ingredient lists
Budget-friendly meal planning
Indian-market suitable meals
4. AI Personal Fitness Coach 🏋️‍♂️🥗

Generates personalized 7-day workout and diet plans.

Features
Workout routines
Indian diet plans
Hydration guidance
Sleep recommendations
Fitness motivation
5. AI Small Business Idea Generator 💼🚀

Creates beginner-friendly startup ideas based on:

User interests
Budget
Location type
Features
Practical startup ideas
Profit estimation
Investment planning
Market suitability analysis
Beginner-friendly recommendations
🧠 Technologies Used

This repository combines Python programming with Generative AI technologies.

Main Technologies
Python
Groq API
LLaMA 3 Models
Python Packages Used
groq
python-dotenv
⚙️ How the Projects Work

Each application follows a similar AI workflow:

Collect user input
Create a structured AI prompt
Send the prompt to Groq API
Generate intelligent AI responses using LLaMA models
Display clean formatted output in the terminal

These projects demonstrate:

Prompt engineering
AI response generation
API integration
User input handling
Real-world AI implementation
📦 Installation

First, clone the repository:

git clone https://github.com/your-username/genai-smart-assistants.git

Move into the project folder:

cd genai-smart-assistants

Install required packages:

pip install groq python-dotenv
🔑 API Key Setup

To run these projects, you need a Groq API key.

Get your API key from:

https://console.groq.com/keys

Create a .env file in the root folder and add:

GROQ_API_KEY=your_api_key_here

Load it in Python using:

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
▶️ Running the Projects

Run any project using:

python main.py

Or navigate into specific project folders and run:

python src/main.py
📂 Full Project Structure
genai-smart-assistants/
│
├── AI-Travel-Planner/
│   │
│   ├── src/
│   │   └── main.py
│   │
│   ├── assets/
│   │   ├── Screenshot 2026-05-23 181232.png
│   │   ├── Screenshot 2026-05-23 181251.png
│   │   └── Screenshot 2026-05-23 181310.png
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
├── AI-Daily-Productivity-Planner/
│   │
│   ├── src/
│   │   └── main.py
│   │
│   ├── assets/
│   │   ├── Screenshot 2026-05-23 174825-1.png
│   │   └── Screenshot 2026-05-23 174802-1.png
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
├── AI-Restaurant-Recommender/
│   │
│   ├── src/
│   │   └── main.py
│   │
│   ├── assets/
│   │   ├── Screenshot 2026-05-23 185018.png
│   │   ├── Screenshot 2026-05-23 184932.png
│   │   └── Screenshot 2026-05-23 184959.png
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
├── AI-Personal-Fitness-Coach/
│   │
│   ├── src/
│   │   └── main.py
│   │
│   ├── assets/
│   │   ├── Screenshot 2026-05-23 190324.png
│   │   ├── Screenshot 2026-05-23 190229.png
│   │   ├── Screenshot 2026-05-23 190247.png
│   │   ├── Screenshot 2026-05-23 190303.png
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
├── AI-Small-Business-Idea-Generator/
│   │
│   ├── src/
│   │   └── main.py
│   │
│   ├── assets/
│   │    ├── Screenshot 2026-05-23 183222.png 
│   │    ├── Screenshot 2026-05-23 183244.png
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
├── requirements.txt
└── README.md
🎯 Learning Outcomes

This repository helps in understanding:

Generative AI applications
Prompt engineering
API integration using Python
Real-world AI systems
Personalized recommendation systems
AI-powered productivity tools
AI travel planning systems
AI food recommendation systems
AI fitness planning systems
AI business recommendation systems
Exception handling
User input management

It is an excellent beginner-to-intermediate level AI project collection for students and aspiring AI developers.

🚨 Error Handling

The projects include exception handling to manage issues such as:

Invalid API keys
Internet connection problems
Groq API rate limits
Model errors
API request failures

This improves reliability and user experience.

🔮 Future Improvements

This repository can be improved further by adding:

Streamlit GUI applications
Voice assistant support
Database integration
AI chatbot interfaces
PDF export systems
Mobile app integration
Real-time AI analytics
Authentication systems
Multi-language support
AI memory systems
Web deployment support
Docker containerization
👨‍💻 Conclusion

The GenAI Smart Assistants Collection demonstrates how Generative AI can be integrated into practical real-world applications using Python and Groq API.

By combining prompt engineering, API integration, and LLaMA models, these applications provide intelligent, personalized, and beginner-friendly AI solutions across multiple domains including productivity, travel, food, health, and entrepreneurship.

This repository is a strong portfolio project for students and beginners who want hands-on experience in AI-powered software development.

❤️ Motivation

“Artificial Intelligence becomes powerful when it solves real human problems intelligently.” 🤖✨

👩‍💻 Author

Dharshini A