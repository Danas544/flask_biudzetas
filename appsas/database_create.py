from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    current_user,
    logout_user,
    login_user,
    UserMixin,  
    login_required,
)

db = SQLAlchemy()
def initialize_db(app):
    db.init_app(app)
    return db




if __name__ == "__main__":
    pass