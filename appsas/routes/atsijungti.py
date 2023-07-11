# pylint: disable-all
from flask import redirect, url_for
from flask_login import logout_user
from appsas import app


@app.route("/atsijungti")
def atsijungti():
    logout_user()
    return redirect(url_for("index"))
