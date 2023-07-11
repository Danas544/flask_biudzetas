# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed
from appsas.models.vartotojas import Vartotojas


class PaskyrosAtnaujinimoForma(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    el_pastas = StringField("El. paštas", [DataRequired()])
    nuotrauka = FileField(
        "Atnaujinti profilio nuotrauką", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Atnaujinti")

    def __init__(self, current_user, *args, **kwargs):
        super(PaskyrosAtnaujinimoForma, self).__init__(*args, **kwargs)
        self.current_user = current_user

    def validate_vardas(self, field):
        Vardas = field.data
        if Vardas == self.current_user.vardas:
            return None
        vartotojas = Vartotojas.query.filter_by(vardas=Vardas).first()
        if vartotojas:
            raise ValidationError("Toks vartotojo vardas jau egzistuoja.")

    def validate_el_pastas(self, naujas_el_pastas):
        if naujas_el_pastas.data != self.current_user.el_pastas:
            vartotojas = Vartotojas.query.filter_by(el_pastas=naujas_el_pastas.data).first()
            if vartotojas:
                raise ValidationError(
                    "Šis el. pašto adresas panaudotas. Pasirinkite kitą."
                )
        else:
            return None
