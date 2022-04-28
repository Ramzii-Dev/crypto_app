from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models.coins import Coin

class AddForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    submit = SubmitField('Add')

