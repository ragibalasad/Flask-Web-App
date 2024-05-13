from flask_login import UserMixin
from . import db


# A database table that contains user informations
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(150))
    dp = db.Column(db.String(150))
    posts = db.relationship("Post")


# Test Object
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
