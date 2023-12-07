from app import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    fName = db.Column(db.String)
    lName = db.Column(db.String)
    pw = db.Column(db.String)

    def __init__(self, email, username, fName, lName, pw):
        self.username = username
        self.email = email
        self.fName = fName
        self.lName = lName
        self.pw = pw


class Posts(db.Model):
    postID = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    path = db.Column(db.String)
    username = db.Column(db.String)
    
    def __init__(self, caption, path, username):
        self.caption = caption
        self.path = path
        self.username = username


class Hearts(db.Model):
    heartID = db.Column(db.Integer, primary_key=True)
    postID = db.Column(db.Integer)
    hearted = db.Column(db.Boolean)
    username = db.Column(db.String)
    
    def __init__(self, postID, hearted, username):
        self.postID = postID
        self.hearted = hearted
        self.username = username
    

class Comments(db.Model):
    commentID = db.Column(db.Integer, primary_key=True)
    postID = db.Column(db.Integer)
    comment = db.Column(db.String)
    username = db.Column(db.String)
    
    def __init__(self, postID, comment, username):
        self.postID = postID
        self.comment = comment
        self.username = username