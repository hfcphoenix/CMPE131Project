from flask_wtf import FlaskForm # uses FlaskForm function from flask_wtf
from wtforms import StringField, PasswordField, BooleanField, SubmitField # uses input fields from wtforms
from wtforms.validators import DataRequired # uses validators from wtforms

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')