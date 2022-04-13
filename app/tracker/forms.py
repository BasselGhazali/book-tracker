from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    image = StringField('Image filename', validators=[DataRequired()])
    submit = SubmitField('Update')
