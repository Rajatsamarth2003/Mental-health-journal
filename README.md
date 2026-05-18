🧠 AI-Powered Mental Health Journal & Chatbot

A modern full-stack web application designed to support mental wellness through journaling, mood tracking, sentiment analysis, and AI-powered emotional support conversations.

Built using:

⚛️ React.js for the frontend
🐍 Flask (Python) for the backend
🗄 SQLite for database management
🤖 AI/NLP for chatbot and sentiment analysis
📌 Overview

The AI-Powered Mental Health Journal & Chatbot helps users maintain emotional well-being by providing a safe digital space to:

✍️ Write daily journal entries
📊 Analyze emotions using sentiment analysis
😊 Track mood history over time
🤖 Chat with an AI-powered supportive chatbot
📈 View emotional insights in a dashboard

The application combines Natural Language Processing (NLP) with a clean and interactive user interface to create a supportive mental wellness platform.

🚀 Features
✍️ Daily Journaling

Users can create and save personal journal entries securely.

🧠 Sentiment Analysis

Each journal entry is analyzed to detect emotional tone such as:

Positive 😊
Neutral 😐
Negative 😔

The backend calculates:

Polarity
Subjectivity

using NLP techniques.

🤖 AI Chatbot Support

An AI chatbot provides supportive responses and conversational interaction for emotional support.

📈 Mood Tracking Dashboard

Visual insights allow users to monitor emotional patterns over time.

💾 Persistent Data Storage

All journal entries and sentiment scores are stored using SQLite database.

🛠 Tech Stack
Technology	Purpose
React.js	Frontend UI
Flask	Backend API
SQLite	Database
Axios	API Communication
Python NLP Libraries	Sentiment Analysis
OpenAI/GPT API	AI Chatbot
📁 Project Structure
Mental health journal/
│
├── backend/
│   ├── app.py                 # Main Flask server
│   ├── chatbot.py             # Chatbot logic
│   ├── sentiment.py           # Sentiment analysis
│   ├── models.py              # Database models
│   └── requirements.txt       # Backend dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html         # Main HTML file
│   │
│   ├── src/
│   │   ├── App.jsx            # Main React component
│   │   ├── index.js           # React entry point
│   │   └── components/
│   │       ├── Chatbot.jsx
│   │       ├── JournalEditor.jsx
│   │       ├── MoodTracker.jsx
│   │       └── Dashboard.jsx
│   │
│   └── package.json
│
├── generate_readme_pdf.py     # Optional PDF generator
└── README.md
⚙️ Backend Functionality

The Flask backend provides REST APIs for handling journals, chatbot communication, and sentiment analysis.

📮 API Endpoints
POST /journal

Saves a journal entry and performs sentiment analysis.

Example Request
{
  "entry": "Today I felt calm and productive."
}
Example Response
{
  "message": "Entry saved",
  "sentiment": {
    "polarity": 0.4,
    "subjectivity": 0.7
  }
}
GET /journals

Returns all saved journal entries.

POST /chat

Receives a user message and returns an AI-generated chatbot response.

Example Request
{
  "message": "I feel stressed today."
}
Example Response
{
  "reply": "I'm sorry you're feeling stressed. Try taking a short break and focusing on your breathing."
}
🗄 Database Schema

The application uses SQLite, a lightweight file-based database.

Journal Table
Field	Type	Description
id	Integer	Primary Key
entry	Text	Journal content
polarity	Float	Sentiment polarity
subjectivity	Float	Sentiment subjectivity
▶️ Running the Backend
Step 1: Open Terminal

Navigate to the backend folder:

cd "C:\Users\rsama\Desktop\Mental health journal\backend"
Step 2: Create Virtual Environment (Optional)
python -m venv venv
Step 3: Activate Virtual Environment
Windows
venv\Scripts\activate
Step 4: Install Dependencies
pip install -r requirements.txt
Step 5: Run Flask Server
python app.py

Backend will start at:

http://127.0.0.1:5000
▶️ Running the Frontend
Step 1: Navigate to Frontend
cd "C:\Users\rsama\Desktop\Mental health journal\frontend"
Step 2: Install Dependencies
npm install
Step 3: Start React App
npm start

Frontend runs at:

http://localhost:3000
🔗 Frontend–Backend Integration

The React frontend communicates with Flask APIs using Axios.

API Calls
POST http://127.0.0.1:5000/chat
POST http://127.0.0.1:5000/journal
GET  http://127.0.0.1:5000/journals

⚠️ Ensure the Flask backend is running before starting the React frontend.

🤖 Customizing Chatbot Responses

To modify chatbot behavior:

Open:

backend/chatbot.py

Edit the function:

def get_chat_response(message):

You can customize:

Tone of responses
Personality style
Advice patterns
Keywords
Emotional support templates
📊 Sentiment Analysis

The sentiment analysis module evaluates emotional tone using NLP libraries such as:

TextBlob
NLTK
Transformers (optional)

The analysis returns:

Polarity
Negative → -1
Neutral → 0
Positive → +1
Subjectivity
Objective → 0
Subjective → 1
🚀 Deployment Options
🌐 Frontend Hosting
▲ Vercel
Netlify
GitHub Pages
⚙️ Backend Hosting
Render
Railway
Deta
🗄 Database Hosting
SQLite (Local)
Supabase PostgreSQL
🔒 Future Improvements

Possible future enhancements include:

🔐 User Authentication
☁️ Cloud Database Integration
📱 Mobile Responsive Design
🧘 Meditation Recommendations
📊 Advanced Mood Analytics
🔔 Daily Reminder Notifications
🎙 Voice-to-Text Journaling
🌍 Multi-language Support
📷 Application Modules
Module	Description
Journal Editor	Write and save personal thoughts
Mood Tracker	Monitor emotional patterns
Dashboard	Visualize mood insights
Chatbot	AI emotional support assistant
💡 Use Cases
Personal emotional wellness tracking
Mental health support companion
NLP-based sentiment analysis learning
Full-stack Flask + React portfolio project
AI chatbot experimentation
📜 License

This project is open-source and available for educational and personal use.

👨‍💻 Author

Developed with ❤️ using Flask, React, and AI technologies.
