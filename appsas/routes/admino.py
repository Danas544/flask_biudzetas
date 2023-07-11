# pylint: disable-all
from flask import redirect, url_for
from flask_login import (current_user, login_required,)
from flask_admin.contrib.sqla import ModelView
from appsas import admin, db, app
from appsas.models.vartotojas import Vartotojas
from appsas.models.irasas import Irasas


class ManoModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.el_pastas == "D@gmail.com":
            adminas = True
            return (
                current_user.is_authenticated
                and current_user.el_pastas == "D@gmail.com"
                and adminas
            )
        else:
            adminas = False
            return adminas


admin.add_view(ManoModelView(Irasas, db.session))
admin.add_view(ManoModelView(Vartotojas, db.session))


# @app.route("/admin")
# @login_required
# def admin():
#     return redirect(url_for(admin))
