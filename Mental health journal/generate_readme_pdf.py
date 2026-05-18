from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Add UTF-8 font
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)

content = """
🧠 AI-Powered Mental Health Journal & Chatbot

Overview
This project is a web application that combines journaling, mood tracking, and an AI-powered chatbot.
Users can write daily journal entries, track mood trends, and interact with a supportive chatbot.

✨ Features
- ✍ Journal Writing
- 😊 Mood Detection
- 🤖 Chatbot Support
- 📊 Mood Dashboard
- 🔒 Data Privacy

⚙️ Tech Stack
- Frontend: React, Axios
- Backend: Flask, Flask-CORS, Flask-SQLAlchemy
- Database: SQLite
- AI / NLP: TextBlob, GPT API

🚀 Usage
1. Start backend: python app.py
2. Start frontend: npm start
3. Open browser: http://localhost:3000
4. Write journal, check mood, chat with bot
"""

pdf.multi_cell(0, 8, content)

pdf.output("Mental_Health_Journal_README.pdf")
print("✅ PDF generated successfully!")
