# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from appsas.forms.slaptazodzio_atnaujinimo_forma import (
    SlaptazodzioAtnaujinimoForma,
    UzklausosAtnaujinimoForma,
)
from appsas.send_email import send_reset_email
from appsas.models.vartotojas import Vartotojas
from appsas import bcrypt, db, app

@app.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = UzklausosAtnaujinimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        send_reset_email(user)
        flash(
            "Jums išsiųstas el. laiškas su slaptažodžio atnaujinimo instrukcijomis.",
            "info",
        )
        return redirect(url_for("prisijungti"))
    return render_template("reset_request.html", title="Reset Password", form=form)


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    user = Vartotojas.verify_reset_token(token)
    if user is None:
        flash("Užklausa netinkama arba pasibaigusio galiojimo", "warning")
        return redirect(url_for("reset_request"))
    form = SlaptazodzioAtnaujinimoForma()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.slaptazodis.data).decode(
            "utf-8"
        )
        user.slaptazodis = hashed_password
        db.session.commit()
        flash("Tavo slaptažodis buvo atnaujintas! Gali prisijungti", "success")
        return redirect(url_for("prisijungti"))
    return render_template("reset_token.html", title="Reset Password", form=form)
