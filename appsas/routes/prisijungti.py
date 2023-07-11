# pylint: disable-all
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user
from appsas import bcrypt
from appsas.forms.prisijungimo_forma import PrisijungimoForma
from appsas.models.vartotojas import Vartotojas
from appsas import app


@app.route("/prisijungti", methods=["GET", "POST"])
def prisijungti():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = PrisijungimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        if user and bcrypt.check_password_hash(user.slaptazodis, form.slaptazodis.data):
            login_user(user, remember=form.prisiminti.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("index"))
        else:
            flash(
                "Prisijungti nepavyko. Patikrinkite el. paštą ir slaptažodį", "danger"
            )
    return render_template("prisijungti.html", title="Prisijungti", form=form)
