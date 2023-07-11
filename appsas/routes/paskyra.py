# pylint: disable-all
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, logout_user
from appsas import bcrypt
from appsas.forms.paskyrosAtnaujinimo_Forma import PaskyrosAtnaujinimoForma
from appsas.forms.slaptazodzio_keitimo_Forma import Slaptazodzio_keitimo_Forma
from appsas.save_pictute import save_picture
from appsas import db, app
from appsas.models.vartotojas import Vartotojas



@app.route("/paskyra", methods=["GET", "POST"])
@login_required
def paskyra():
    form = PaskyrosAtnaujinimoForma(current_user)
    if form.validate_on_submit():
        if form.nuotrauka.data:
            nuotrauka = save_picture(form.nuotrauka.data)
            current_user.nuotrauka = nuotrauka
        current_user.vardas = form.vardas.data
        current_user.el_pastas = form.el_pastas.data
        db.session.commit()
        flash("Tavo paskyra atnaujinta!", "success")
        return redirect(url_for("paskyra"))
    elif request.method == "GET":
        form.vardas.data = current_user.vardas
        form.el_pastas.data = current_user.el_pastas
    nuotrauka = url_for(
        "static", filename="profilio_nuotraukos/" + current_user.nuotrauka
    )
    return render_template(
        "paskyra.html", title="Account", form=form, nuotrauka=nuotrauka
    )


@app.route("/keitimas", methods=["GET", "POST"])
@login_required
def keitimas():
    form = Slaptazodzio_keitimo_Forma()
    if form.validate_on_submit():
        if bcrypt.check_password_hash(
            current_user.slaptazodis, form.old_slaptazodis.data
        ):
            koduotas_slaptazodis = bcrypt.generate_password_hash(
                form.new_slaptazodis.data
            ).decode("utf-8")
            user = db.session.get(Vartotojas, current_user.id)
            user.slaptazodis = koduotas_slaptazodis
            db.session.add(user)
            db.session.commit()
            logout_user()
            flash(
                "Sėkmingai pakeistas slaptažodis, galite prisijungti per naujo", "info"
            )
            return redirect(url_for("index"))
        else:
            flash("Neteisingas dabartinis slaptažodis", "danger")
    return render_template("keitimas.html", title="Keitimas slaptažodžio", form=form)
