from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AddProduct(FlaskForm):
    id_ = StringField('id')
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description')
    img_name = StringField('img_name')
    price = StringField('price', validators=[DataRequired()])
    add = SubmitField('add')
