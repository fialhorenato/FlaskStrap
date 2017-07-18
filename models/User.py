from models.Shared import db
from flask import jsonify

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    pass


    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def _toJson_(self):
        response = jsonify({
                    'id': self.id,
                    'username':self.username,
                    'email': self.email,
        })
        return response