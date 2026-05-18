# 🧠 AI-Powered Mental Health Journal & Chatbot

A complete journaling, mood analysis, and AI chatbot support web application built using **Flask (Python)** and **React.js**.

---

# 📌 Overview

The AI-Powered Mental Health Journal & Chatbot helps users maintain emotional wellness through journaling, mood tracking, sentiment analysis, and supportive AI conversations.

Users can:

- ✍️ Write daily journal entries
- 😊 Analyze emotions using sentiment analysis
- 📊 Track mood over time
- 🤖 Chat with an AI-powered supportive chatbot
- 📈 View emotional insights in a dashboard

The backend is developed using **Flask**, **SQLite**, and **NLP-based sentiment analysis**, while the frontend is built using **React.js**.

---

# 🚀 Features

## ✍️ Daily Journal Entries
Users can securely write and save personal journal entries.

## 🧠 Sentiment Analysis
Each journal entry is analyzed to determine emotional tone:

- Positive 😊
- Neutral 😐
- Negative 😔

The system calculates:
- Polarity
- Subjectivity

## 🤖 AI Chatbot Support
An AI-powered chatbot provides supportive and conversational responses.

## 📈 Mood Tracking Dashboard
Users can visualize emotional trends and mood history over time.

## 💾 Database Storage
All journal entries and sentiment results are stored using SQLite database.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| React.js | Frontend UI |
| Flask | Backend API |
| SQLite | Database |
| Axios | API Communication |
| Python NLP Libraries | Sentiment Analysis |
| OpenAI/GPT API | AI Chatbot |

---

# 📁 Project Structure

```bash
Mental health journal/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── sentiment.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── components/
│   │       ├── Chatbot.jsx
│   │       ├── JournalEditor.jsx
│   │       ├── MoodTracker.jsx
│   │       └── Dashboard.jsx
│   │
│   └── package.json
│
├── generate_readme_pdf.py
└── README.md

⚙️ Backend Functionality

The Flask backend provides REST APIs for journaling, sentiment analysis, and chatbot communication.

📮 API Endpoints
POST /journal
Saves a journal entry and returns sentiment analysis.
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

🗄 Database Schema
The project uses SQLite database.
Journal Table

| Field        | Type    | Description            |
| ------------ | ------- | ---------------------- |
| id           | Integer | Primary Key            |
| entry        | Text    | Journal content        |
| polarity     | Float   | Sentiment polarity     |
| subjectivity | Float   | Sentiment subjectivity |


▶️ Running the Backend
Step 1: Open Terminal
cd "C:\Users\rsama\Desktop\Mental health journal\backend"
Step 2: Create Virtual Environment (Optional)
python -m venv venv
Step 3: Activate Virtual Environment
Windows
venv\Scripts\activate
Step 4: Install Dependencies
pip install -r requirements.txt
Step 5: Run Flask Backend
python app.py
Backend will run at:  http://127.0.0.1:5000


▶️ Running the Frontend
Step 1: Navigate to Frontend Folder
cd "C:\Users\rsama\Desktop\Mental health journal\frontend"
Step 2: Install Dependencies
npm install
Step 3: Run React Frontend
npm start
Frontend will run at: http://localhost:3000


🔗 Frontend–Backend Connection
The React frontend communicates with Flask APIs using Axios.
API Calls
POST http://127.0.0.1:5000/chat
POST http://127.0.0.1:5000/journal
GET  http://127.0.0.1:5000/journals
⚠️ Make sure the backend server is running before starting the frontend.


🤖 Customizing Chatbot Replies
Open:  backend/chatbot.py


📊 Sentiment Analysis
The application uses NLP libraries such as:
-TextBlob
-NLTK
-Transformers (optional)
Sentiment analysis returns:
-Polarity
-Subjectivity

🚀 Deployment Options
**Frontend Hosting**
-Vercel
-Netlify
-GitHub Pages

**Backend Hosting**
-Render.com
-Railway.app
-Deta Space

**Database Hosting**
-SQLite
-Supabase PostgreSQL

🔒 Future Improvements
-User Authentication
-Cloud Database Integration
-Mood Analytics
-Daily Reminders
-Voice-to-Text Journaling
-Multi-language Support
-Meditation Recommendations
