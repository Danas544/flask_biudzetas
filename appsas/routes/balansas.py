# pylint: disable-all
from flask import render_template
from flask_login import current_user, login_required
from appsas.models.irasas import Irasas
from appsas import app




@app.route("/balansas")
@login_required
def balance():
    try:
        visi_irasai = Irasas.query.filter_by(vartotojas_id=current_user.id)
    except:
        visi_irasai = []
    balansas = 0
    for irasas in visi_irasai:
        if irasas.pajamos:
            balansas += irasas.suma
        else:
            balansas -= irasas.suma
    return render_template("balansas.html", balansas=balansas)
