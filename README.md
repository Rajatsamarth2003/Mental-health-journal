🧠 AI-Powered Mental Health Journal & Chatbot
A complete journaling, mood analysis, and chatbot support web application built using Flask (Python) and React (Frontend).

📌 Overview

This project helps users maintain their mental wellness by allowing them to:

Write daily journal entries

Get sentiment analysis (positive/negative/neutral)

Track their mood over time

Chat with an AI-powered supportive chatbot

View insights in a dashboard

The backend uses Flask, SQLite, NLP sentiment analysis, and an AI chatbot API.
The frontend is built with React.

📁 Project Structure
Mental health journal/
│
├── backend/
│   ├── app.py               # Main Flask server
│   ├── chatbot.py           # Chatbot logic
│   ├── sentiment.py         # Sentiment analysis script
│   ├── models.py            # Database models
│   └── requirements.txt     # Backend dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html       # Main HTML file
│   ├── src/
│   │   ├── App.jsx          # Main React Component
│   │   ├── index.js         # React entry file
│   │   └── components/      # UI components
│   │       ├── Chatbot.jsx
│   │       ├── JournalEditor.jsx
│   │       ├── MoodTracker.jsx
│   │       └── Dashboard.jsx
│   ├── package.json
│
├── generate_readme_pdf.py   # Optional – generates README PDF
└── README.md                # Project documentation

⚙️ How the Backend Works

Your Flask backend exposes these routes:

POST /journal

Saves a journal entry and returns sentiment score.
Example response:

{
  "message": "Entry saved",
  "sentiment": {
    "polarity": 0.4,
    "subjectivity": 0.7
  }
}

GET /journals

Returns all journal entries saved in the database.

POST /chat

Receives user message → returns chatbot reply using GPT.

🗄 Database

This project uses SQLite, a lightweight file-based database.
Schema includes:

Journal table
Field	Type	Description
id	Integer	Primary key
entry	Text	Journal content
polarity	Float	Sentiment polarity
subjectivity	Float	Sentiment subjectivity
▶️ How to Run the Backend
1. Open terminal in backend folder:
cd "C:\Users\rsama\Desktop\Mental health journal\backend"

2. (Optional) Create virtual environment
python -m venv venv

3. Activate virtual environment
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run Flask backend
python app.py


Backend will run at:

http://127.0.0.1:5000

▶️ How to Run the Frontend
1. Enter frontend folder
cd "C:\Users\rsama\Desktop\Mental health journal\frontend"

2. Install Node.js dependencies
npm install

3. Run frontend
npm start


Frontend runs at:

http://localhost:3000

🔗 Frontend–Backend Connection

Your React app uses Axios to call:

POST http://127.0.0.1:5000/chat

POST http://127.0.0.1:5000/journal

GET http://127.0.0.1:5000/journals

Make sure backend is running before frontend.

🤖 How to Modify Chatbot Replies

Open:

backend/chatbot.py


Inside:

def get_chat_response(message):


Modify:

Tone

Personality

Type of advice

Keywords

Message templates

🚀 Deployment (Free Options)
Frontend:

Netlify

GitHub Pages

Vercel

Backend:

Render.com (best free Python hosting)

Railway.app

Deta Space

Database:

SQLite (local)

Supabase (free cloud PostgreSQL)
