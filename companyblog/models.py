from email.policy import default
from companyblog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    profile_pic = db.Column(db.String(20), index = True, nullable = False, default = 'default.png')
    email = db.Column(db.String(64), index = True, unique = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(128))

    posts = db.relationship('BlogPost', backref = 'author', lazy = True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_hashed_password(self, password):
        return check_password_hash(self.password_hash, password=password)
    
    def __repr__(self) -> str:
        return "Username: {self.username}"

class BlogPost(db.Model):
    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    title = db.Column(db.String(140), nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    text = db.Column(db.Text, nullable = False)

    def __init__(self, title, user_id, text) -> None:
        self.title = title
        self.user_id = user_id
        self.text = text

    def __repr__(self) -> str:
        return f"Title: {self.title}"