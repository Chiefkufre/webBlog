from . import db
from flask_login import UserMixin
from datetime import datetime


class BlogContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(200), nullable=False, default='N/A')
    password = db.Column(db.String(50), nullable=False)
    content = db.relationship('BlogContent')
    
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)
    
    

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(200), nullable=False, default='N/A')
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text,nullable=False )
   

    
