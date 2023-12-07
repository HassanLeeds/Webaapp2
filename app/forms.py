from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, StringField, FileField, PasswordField, HiddenField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=1, max=100)])
    pw = PasswordField('Password', validators = [DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=1, max=100)])
    email = EmailField('Email', validators = [DataRequired(), Length(min=1, max=100)])
    fName = StringField('First Name', validators = [DataRequired(), Length(min=1, max=100)])
    lName = StringField('Last Name', validators = [DataRequired(), Length(min=1, max=100)])
    pw = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=100)])
    pw2 = PasswordField('Confirm Password', validators = [DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    post = FileField('post')
    caption = TextAreaField('Make a Post', validators = [Length(max=1000)])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = StringField('Make a Comment', validators = [Length(min=1, max=100)])
    submit = SubmitField('Post')
    postID = HiddenField('Post ID')
