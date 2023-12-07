from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, StringField, FileField, PasswordField, HiddenField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired(), Length(min=1, max=100)])
    pw = PasswordField('pw', validators = [DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('username', validators = [DataRequired(), Length(min=1, max=100)])
    email = EmailField('email', validators = [DataRequired(), Length(min=1, max=100)])
    fName = StringField('fName', validators = [DataRequired(), Length(min=1, max=100)])
    lName = StringField('lName', validators = [DataRequired(), Length(min=1, max=100)])
    pw = PasswordField('pw', validators = [DataRequired(), Length(min=6, max=100)])
    pw2 = PasswordField('pw2', validators = [DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    post = FileField('post')
    caption = TextAreaField('caption', validators = [Length(min=1, max=1000)])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = StringField('comment', validators = [Length(min=1, max=100)])
    submit = SubmitField('Comment')
    postID = HiddenField('Post ID')
