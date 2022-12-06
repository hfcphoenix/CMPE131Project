from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember me?')
    submit = SubmitField('Sign In')
    recaptcha = RecaptchaField()

class CreateAccountForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Create Account')
    recaptcha = RecaptchaField()

class UpdatePasswordForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Update Account')

class AddFollowingForm(FlaskForm):
    username = StringField('Enter the person you would like to follow', validators = [DataRequired()])
    submit = SubmitField('Follow')

class RemoveFollowingForm(FlaskForm):
    username = StringField('Enter the person you want to stop following', validators = [DataRequired()])
    submit = SubmitField('Remove')