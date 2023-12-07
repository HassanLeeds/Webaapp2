from flask import render_template, flash, request, session, redirect, url_for, jsonify
from app import app, models, db
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
import os
from datetime import datetime
import uuid
import sys

from .forms import LoginForm, RegisterForm, PostForm, CommentForm


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(userID):
    return models.Users.query.get(int(userID))

@app.route('/', methods=["GET", "POST"])
@login_required
def home():
    comment_form = CommentForm()
    post_form = PostForm()
    user = current_user
    user_hearts = set(heart.postID for heart in models.Hearts.query.filter_by(username=user.username))
    if request.method == "POST":
        if post_form.validate_on_submit():
            # Handle post submission
            post = post_form.post.data
            caption = request.form["caption"]
            print("lol", file=sys.stderr)
            if post:
                unique_filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
                original_filename = secure_filename(post.filename)
                _, original_extension = os.path.splitext(original_filename)
                filename = unique_filename + original_extension.lower()
                file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename)
                post.save(file_path)
                new_post = models.Posts(username=user.username, path=app.config['UPLOAD_FOLDER']+"/"+filename, caption=caption)
            else:
                new_post = models.Posts(username=user.username, path="NA", caption=caption)
            db.session.add(new_post)
            db.session.commit()
    posts = reversed(models.Posts.query.all())
    comments = list(reversed(models.Comments.query.all()))
    if user:
        return render_template("home.html", title="Home", posts=posts, comment_form=comment_form, post_form=post_form, comments=comments, hearts = user_hearts, page="home", user=user)
    else:
        return redirect(url_for("login"))
        

@app.route('/comment/<int:postID>', methods=["GET", "POST"])
@login_required
def comment(postID):
    user = current_user
    comment_content = request.json['comment']
    comment = models.Comments(postID=postID, comment=comment_content, username=user.username)
    db.session.add(comment)
    db.session.commit()

    return jsonify({
        'result': 'success',
        'comment': {
            'content': comment.comment,
            'username': comment.username,
        }
    })

@app.route('/heart/<int:postID>', methods=["GET", "POST"])
@login_required
def heart(postID):
    user = current_user
    hearted = request.json['heart']
    existing_like = models.Hearts.query.filter_by(postID=postID, username=user.username).first()

    if existing_like:
        # User has already liked the post, delete the like
        db.session.delete(existing_like)
        hearted = False  # Indicate that the post is no longer liked
    else:
        # User hasn't liked the post, add the like
        heart = models.Hearts(postID=postID, hearted=hearted, username=user.username)
        hearted = True  # Indicate that the post is now likedheart = models.Hearts(postID=postID, hearted=hearted, username=user.username)
        db.session.add(heart)
    db.session.commit()

    return jsonify({
        'result': 'success',
        'heart': hearted
    })

@app.route('/<string:username>', methods=["GET", "POST"])
@login_required
def profile(username):
    comment_form = CommentForm()
    user = current_user
    user_hearts = set(heart.postID for heart in models.Hearts.query.filter_by(username=user.username))
    posts = reversed(list(models.Posts.query.filter_by(username=username)))
    comments = list(reversed(models.Comments.query.all()))
    if user:
        return render_template("profile.html", title="Profile", posts=posts, comment_form=comment_form, comments=comments, hearts = user_hearts, page="home", user=user)
    else:
        return redirect(url_for("login"))

@app.route('/likes', methods=["GET", "POST"])
@login_required
def likes():
    comment_form = CommentForm()
    user = current_user
    user_hearts = set(heart.postID for heart in models.Hearts.query.filter_by(username=user.username))
    posts = [heart.postID for heart in models.Hearts.query.filter_by(username=user.username, hearted=True)]
    comments = list(reversed(models.Comments.query.all()))
    hearted_posts =reversed(models.Posts.query.filter(models.Posts.postID.in_(posts)).all())
    if user:
        return render_template("liked.html", title="Profile", posts=hearted_posts, comment_form=comment_form, comments=comments, hearts = user_hearts, page="home", user=user)
    else:
        return redirect(url_for("login"))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        username = request.form["username"]
        pw = request.form["pw"]
        user = models.Users.query.filter_by(username=username).first()
        if user and pw == user.pw:
            login_user(user)
            return redirect(url_for("home"))
        elif not user:
            if form.validate_on_submit():
                flash("User Does not Exist.")
        elif pw != user.pw:
            if form.validate_on_submit():
                flash("Password Incorrect.")
    return render_template("login.html", title="Login", form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        email = request.form["email"]
        fName = request.form["fName"]
        lName = request.form["lName"]
        username = request.form["username"]
        pw = request.form["pw"]
        pw2 = request.form["pw2"]

        if models.Users.query.filter_by(username=username):
            flash("Username already in use!")
            return render_template("register.html", title="Register", form=form)

        elif models.Users.query.filter_by(email=email):
            flash("Email already in use!")
            return render_template("register.html", title="Register", form=form)

        elif pw != pw2:
            flash("Passwords must match!")
            return render_template("register.html", title="Register", form=form)

        newUser = models.Users(email = email, fName = fName, lName = lName,
                            pw = pw, username = username)
        db.session.add(newUser)
        db.session.commit()
        flash("Registered Successfuly")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged Out")
    return redirect(url_for("login"))