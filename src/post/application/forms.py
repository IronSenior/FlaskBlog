from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    subtitle = StringField('Subtitle', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Registrar')