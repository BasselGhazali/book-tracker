from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrationForm(FlaskForm):

    name = StringField('Name')
    email = StringField('Email')
    submit = SubmitField('Register')
