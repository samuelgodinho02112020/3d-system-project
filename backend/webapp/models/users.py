from webapp import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    password = db.Column(db.Text, nullable = False)
    phone_number = db.Column(db.String(10), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    dob = db.Column(db.Date, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 



    