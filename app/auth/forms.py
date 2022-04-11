from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email already exists')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),
                                           Length(3, 15, message='Username must be between 3 and 15 characters')])
    email = StringField('Email', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(5, message='Password must be greater than 4 characters'),
                                                     EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_logged_in = BooleanField('Stay logged in')
    submit = SubmitField('Log in')
