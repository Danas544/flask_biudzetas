# pylint: disable-all
from flask import render_template
from appsas import db, app
from appsas.models.vartotojas import Vartotojas
from appsas.routes.admino import ManoModelView


@app.route("/")
def index():
    adminas = ManoModelView(Vartotojas, db.session)
    adminas = adminas.is_accessible()
    print(adminas)
    return render_template("index.html", adminas=adminas)
