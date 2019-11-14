from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddProduct(FlaskForm):
    id = ''
    name = StringField('Name product', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    img = FileField('Get image')
    price = StringField('Add price', validators=[DataRequired()])
    add = SubmitField('add')
