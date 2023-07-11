
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired,  EqualTo





class Slaptazodzio_keitimo_Forma(FlaskForm):
    old_slaptazodis = PasswordField('Dabartinis slaptažodis', [DataRequired()])
    new_slaptazodis = PasswordField('Naujas slaptažodis', [DataRequired()])
    new_patvirtintas_slaptazodis = PasswordField("Pakartokite nauja slaptažodį", [EqualTo('new_slaptazodis', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Pakeisti')

