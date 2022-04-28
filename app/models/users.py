from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    coins = db.relationship('Coin', backref='owner', lazy='True')

    def __init__(self, username, email, password,coins):
        self.username = username
        self.email = email
        self.password = password
        self.coins = coins
        
    def __repr__(self):
        return '<User %r>' % self.username