# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField,  StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from appsas.models.vartotojas import Vartotojas





class RegistracijosForma(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    el_pastas = StringField('El. paštas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    patvirtintas_slaptazodis = PasswordField("Pakartokite slaptažodį", [EqualTo('slaptazodis', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Prisiregistruoti')

    def validate_vardas(self, field):
        Vardas = field.data
        vartotojas = Vartotojas.query.filter_by(vardas=Vardas).first()
        if vartotojas:
            raise ValidationError("Toks vartotojo vardas jau egzistuoja.")

    def validate_el_pastas(self, naujas_el_pastas):
        vartotojas = Vartotojas.query.filter_by(el_pastas=naujas_el_pastas.data).first()
        if vartotojas:
            raise ValidationError(
                "Šis el. pašto adresas panaudotas. Pasirinkite kitą."
            )
