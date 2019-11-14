from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddSupermarket(FlaskForm):
    id = ''
    name = StringField('Name Supermarket', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    img = FileField('Get image')
    add = SubmitField('add')
