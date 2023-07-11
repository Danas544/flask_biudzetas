# pylint: disable-all
from appsas import app, db

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
    db.create_all()