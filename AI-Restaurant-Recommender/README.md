AI Restaurant Recommender 🍽️🤖
>🚀 Built as a real-world AI food recommendation system using Groq API + LLaMA models

An intelligent AI-powered restaurant and meal recommendation system that generates healthy, budget-friendly, and personalized meal suggestions using Groq API (LLaMA models).

📖 Project Overview

The AI Restaurant Recommender is a beginner-friendly Python application that helps users discover suitable meals based on their food preferences, budget, cuisine choices, and health goals using Artificial Intelligence.

Instead of manually searching for healthy and affordable food options, users simply enter their preferences. The AI system then generates personalized meal recommendations including ingredients, estimated costs, calorie information, and health benefits.

This project demonstrates how Generative AI can be used to build smart food recommendation systems, nutrition planning tools, and personalized meal assistants.

The application uses the Groq API with LLaMA models to generate realistic, practical, and beginner-friendly meal suggestions suitable for Indian users and daily lifestyles.

✨ Features

The application generates complete AI-powered meal recommendations including:

Personalized meal suggestions
Budget-friendly food recommendations
Cuisine-based meal planning
Health-goal-based meal ideas
Estimated meal cost
Approximate calorie information
Simple ingredient lists
Indian market suitable meals
Easy-to-cook meal ideas
Beginner-friendly recommendation system
Dynamic AI-generated suggestions
Clean terminal-based interaction

The generated meal recommendations change dynamically based on:

Food preference
Budget per meal
Cuisine type
Health goals
🧠 Technologies Used

This project combines Python programming with Generative AI technology.

Main Technologies
Python
Groq API (LLaMA 3 models)
Python Packages Used
groq
python-dotenv
⚙️ How the Project Works

The program first asks the user for important food-related information such as food preference, meal budget, cuisine type, and health goals.

After collecting the inputs, the application creates a structured AI prompt and sends it to the Groq API using LLaMA models.

The AI model analyzes the user's food preferences and generates personalized meal recommendations including:

Meal names
Ingredient lists
Estimated costs
Approximate calories
Health suitability explanations

Finally, the generated meal recommendations are displayed directly in the terminal.

📥 User Inputs

The system collects the following information from the user:

Input	Purpose
Food Preference	Determines meal type
Budget per Meal	Controls affordability
Cuisine Type	Personalized cuisine selection
Health Goal	Nutrition-focused recommendations
🍛 Example Inputs
Food Preferences
Veg
Non-Veg
Vegan
Jain
Eggetarian
Cuisine Types
Indian
Chinese
Italian
South Indian
North Indian
Continental
Health Goals
Weight Loss
Muscle Gain
Healthy Eating
High Protein
Normal Diet
📸 Project Output

💡 Example Output
============================================================
        AI RESTAURANT RECOMMENDER
============================================================
Enter food preference (veg/non-veg/vegan/etc): non-veg
Enter your budget per meal (₹): 200
Enter cuisine type (Indian/Chinese/Italian/etc): indian
Enter health goal (weight loss/muscle gain/normal): normal

Generating meal recommendations...

============================================================
        YOUR MEAL RECOMMENDATIONS
============================================================

Here are 5 meal ideas based on the user's preferences:

### Meal 1: Chicken Biryani
1. **Meal Name**: Chicken Biryani
2. **Ingredients**: 
   - Basmati rice
   - Chicken breast
   - Onions
   - Tomatoes
   - Garlic
   - Ginger
   - Cumin seeds
   - Coriander powder
   - Salt
3. **Estimated Cost**: ₹180
4. **Calories**: 550 approx
5. **Why it is suitable**: This meal is a classic Indian dish that is easy to cook and can be found in most Indian restaurants. It's a balanced meal with carbohydrates from rice, protein from chicken, and fiber from onions and tomatoes, all within the budget.

### Meal 2: Tandoori Chicken with Roti
1. **Meal Name**: Tandoori Chicken with Roti
2. **Ingredients**: 
   - Chicken breast
   - Yogurt
   - Lemon juice
   - Garam masala
   - Cilantro
   - Roti (whole wheat flatbread)
   - Onions
   - Cucumber
3. **Estimated Cost**: ₹190
4. **Calories**: 420 approx
5. **Why it is suitable**: Tandoori chicken is a popular Indian dish that is high in protein and can be paired with whole wheat roti for a balanced meal. The addition of onions and cucumber provides extra fiber and vitamins.

### Meal 3: Fish Curry with Brown Rice
1. **Meal Name**: Fish Curry with Brown Rice
2. **Ingredients**: 
   - Fish fillet (any white fish)
   - Onions
   - Tomatoes
   - Garlic
   - Ginger
   - Turmeric
   - Coriander powder
   - Brown rice
3. **Estimated Cost**: ₹200
4. **Calories**: 500 approx
5. **Why it is suitable**: Fish is a great source of protein and omega-3 fatty acids. Paired with brown rice, which is high in fiber, this meal provides a good balance of nutrients. The use of turmeric and coriander powder adds anti-inflammatory properties.

### Meal 4: Chicken and Vegetable Kabab
1. **Meal Name**: Chicken and Vegetable Kabab
2. **Ingredients**: 
   - Chicken breast
   - Bell peppers
   - Onions
   - Tomatoes
   - Cucumber
   - Yogurt
   - Cumin seeds
3. **Estimated Cost**: ₹170
4. **Calories**: 380 approx
5. **Why it is suitable**: Kababs are easy to cook and can be made with a variety of vegetables, making them a healthy and balanced option. The addition of yogurt provides extra calcium and protein.

### Meal 5: Egg Curry with Whole Wheat Roti
1. **Meal Name**: Egg Curry with Whole Wheat Roti
2. **Ingredients**: 
   - Eggs
   - Onions
   - Tomatoes
   - Garlic
   - Ginger
   - Turmeric
   - Coriander powder
   - Whole wheat roti
3. **Estimated Cost**: ₹160
4. **Calories**: 400 approx
5. **Why it is suitable**: Egg curry is a budget-friendly and protein-rich meal option. Paired with whole wheat roti, it provides a good balance of carbohydrates, protein, and fiber, making it a practical and healthy choice.

============================================================
MEALS GENERATED SUCCESSFULLY ✅
Eat healthy • Stay fit • Stay strong 💪
============================================================
## 📂 Project Structure
AI-Restaurant-Recommender/
│
├── src/
│   └── main.py
│
├── assets/
│   ├── Screenshot 2026-05-23 185018.png
│   ├── Screenshot 2026-05-23 184932.png
│   ├── Screenshot 2026-05-23 184959.png>
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
📦 Installation

First, install the required packages:

pip install groq python-dotenv
🔑 API Key Setup

To use this project, you need a Groq API key.

Get your API key from:

https://console.groq.com/keys

After generating the API key, create a .env file and add:

GROQ_API_KEY=your_api_key_here

Then the code will automatically load it using:

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
▶️ Running the Project

Run the Python file using:

python main.py

The application will ask for food-related details and then generate personalized meal recommendations automatically.

🎯 Learning Outcomes

This project helps in understanding:

AI-powered recommendation systems
Prompt engineering
API integration using Python
User input handling
Exception handling
Nutrition recommendation systems
Personalized AI applications
Real-world AI implementation

It is an excellent beginner project for students who want practical experience in integrating Artificial Intelligence with food and health recommendation systems.

🚨 Error Handling

The project includes exception handling to manage issues such as:

Invalid model name
Groq API rate limits
API request failures
Internet connection issues

This improves the reliability and user experience of the application.

🔮 Future Improvements

This project can be improved further by adding:

GUI using Tkinter or Streamlit
Restaurant API integration
Food delivery integration
PDF meal plan export
Voice assistant support
Diet tracking system
Mobile app integration
Multi-language support
BMI calculator
AI nutrition analytics
Weekly meal planner
👨‍💻 Conclusion

The AI Restaurant Recommender is a practical and beginner-friendly AI project that demonstrates how Generative AI can help users discover healthy, affordable, and personalized meals within seconds.

By combining Python with the Groq API, this application creates smart meal recommendations based on user preferences, budget, cuisine choices, and health goals.

It is a great project for students and beginners who want to explore AI-powered software development and recommendation systems.

❤️ Motivation

“Healthy eating is not a diet — it is a lifestyle.” 🍽️💪

Author

Dharshini A


![alt text](<Screenshot 2026-05-23 185018.png>) ![alt text](<Screenshot 2026-05-23 184932.png>) ![alt text](<Screenshot 2026-05-23 184959.png>)