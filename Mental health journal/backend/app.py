from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_chat_response
from sentiment import analyze_sentiment
from models import db, Journal

app = Flask(__name__)
CORS(app)  # allow frontend requests
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/journal', methods=['POST'])
def journal_entry():
    data = request.json
    text = data['entry']
    sentiment = analyze_sentiment(text)

    new_entry = Journal(entry=text, polarity=sentiment['polarity'], subjectivity=sentiment['subjectivity'])
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'message': 'Entry saved', 'sentiment': sentiment})

@app.route('/journals', methods=['GET'])
def get_journals():
    entries = Journal.query.all()
    return jsonify([{"id": e.id, "entry": e.entry, "polarity": e.polarity, "subjectivity": e.subjectivity} for e in entries])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    reply = get_chat_response(user_input)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
