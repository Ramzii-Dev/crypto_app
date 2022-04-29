from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models.coins import Coin
import os
import json

abs = os.path.abspath('.')
path_file = os.path.join(abs, 'app\\helpers\\coins.json')
with open(path_file, 'r') as f:
    data = json.load(f)
names = []
for i in data:
    names.append(i['name'])
    
class AddForm(FlaskForm):
    name = SelectField('name',choices=names)
    value = StringField('Value', validators=[DataRequired()])
    submit = SubmitField('Add')

