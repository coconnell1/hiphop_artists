from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CreateArtist(FlaskForm):
    name = StringField('Artists Name', validators=[DataRequired()])
    birth = StringField('Birth', validators=[DataRequired()])
    music = TextAreaField('Music Description', validators=[DataRequired()])
    events = TextAreaField('Events', validators=[DataRequired()])
    submit = SubmitField('Create New Artist')
