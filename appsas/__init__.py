# pylint: disable-all
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "4654f5dfadsrfasdr54e6rae"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "biudzetas.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "moterisarbavyras@gmail.com"
app.config["MAIL_PASSWORD"] = "jlgltculfzfjzcrx"

admin = Admin(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = "prisijungti"
login_manager.login_message = "User needs to be logged in to view this page"
login_manager.login_message_category = "info"
db = None


from appsas.database_create import initialize_db

db = initialize_db(app)

from appsas.models.vartotojas import Vartotojas



@login_manager.user_loader
def load_user(vartotojo_id: str) -> Vartotojas:
    return Vartotojas.query.get(int(vartotojo_id))


import appsas.routes.index_default 
import appsas.routes.admino
import appsas.routes.paskyra
import appsas.routes.registruotis
import appsas.routes.irasai
import appsas.routes.forget_password
import appsas.routes.balansas
import appsas.routes.atsijungti
import appsas.routes.prisijungti


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
