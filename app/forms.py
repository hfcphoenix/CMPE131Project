from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm): # form to collect login information
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember me?') # allows user to stay logged in
    submit = SubmitField('Sign In')
    recaptcha = RecaptchaField()

class CreateAccountForm(FlaskForm): # form to collect information to create an account
    email = StringField('Email', validators = [DataRequired(), Email()]) # data required makes sure box is filled, email makes sure its an email
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Create Account')
    recaptcha = RecaptchaField() # anti-bot captcha system

class UpdatePasswordForm(FlaskForm): # form to collect information to update password
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Update Account')

class AddFollowingForm(FlaskForm): # form to collect information on user to follow
    username = StringField('Enter the person you would like to follow', validators = [DataRequired()])
    submit = SubmitField('Follow')

class RemoveFollowingForm(FlaskForm): # form to collect information on user to stop following
    username = StringField('Enter the person you want to stop following', validators = [DataRequired()])
    submit = SubmitField('Remove')