from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    image = StringField('Image filename', validators=[DataRequired()])

    submit = SubmitField('Update')


class CreateBookForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    image = StringField('Image filename', validators=[DataRequired()])
    tags = StringField('Tags')
    vendors = StringField('Vendors')
    genre = StringField('Genre')

    submit = SubmitField('Update')


class AddBookForm(FlaskForm):
    pub_id = IntegerField('Publisher ID')
