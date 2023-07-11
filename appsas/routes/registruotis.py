# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from appsas import db, bcrypt, app
from appsas.forms.registracijos_forma import RegistracijosForma
from appsas.models.vartotojas import Vartotojas


@app.route("/registruotis", methods=["GET", "POST"])
def registruotis():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistracijosForma()
    if form.validate_on_submit():
        koduotas_slaptazodis = bcrypt.generate_password_hash(
            form.slaptazodis.data
        ).decode("utf-8")
        vartotojas = Vartotojas(
            vardas=form.vardas.data,
            el_pastas=form.el_pastas.data,
            slaptazodis=koduotas_slaptazodis,
        )
        db.session.add(vartotojas)
        db.session.commit()
        flash("Sėkmingai prisiregistravote! Galite prisijungti", "success")
        return redirect(url_for("index"))
    return render_template("registruotis.html", title="Register", form=form)
