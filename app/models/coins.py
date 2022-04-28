from . import db 
from datetime import datetime 

class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    value = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, value, user_id):
        self.name = name
        self.value = value
        self.user_id = user_id

    def __repr__(self):
        return '<Coin %r>' % self.name