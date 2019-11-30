from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')



class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Subtítulo', validators=[Length(max=128)])
    content = TextAreaField('Contenido', validators=[DataRequired()])
    submit = SubmitField('Enviar')

    