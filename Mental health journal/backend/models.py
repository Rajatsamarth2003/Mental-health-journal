from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.Text, nullable=False)
    polarity = db.Column(db.Float)
    subjectivity = db.Column(db.Float)
