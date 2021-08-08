from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class BienForm(FlaskForm):
    name = StringField('Nom du bien', validators=[DataRequired(), Length(1, 64)])
    typeBien = StringField('Type du bien', validators=[DataRequired(), Length(1, 64)])
    adresseBien =StringField('Adresse du bien', validators=[DataRequired(), Length(1, 60)])
    descriptionBien = TextAreaField('Description du bien', validators=[DataRequired(), Length(1, 100)])
    firstname = StringField('Prenom', validators=[DataRequired(), Length(1, 64)])
    lastname = StringField('Nom', validators=[DataRequired(), Length(1, 64)])
    adresse =StringField('Adresse', validators=[DataRequired(), Length(1, 60)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    telephone = StringField('Telephone', validators=[DataRequired(), Length(1, 25)])
    submit = SubmitField('Save')