from datetime import timedelta

from flask import Flask

from db import db
from res.staff import staff
from res.room import room
from res.tenants import tenants
from config import run_config
from  res.create_db import create_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(create_db)
    app.register_blueprint(staff)
    app.register_blueprint(room)
    app.register_blueprint(tenants)

    return app


if __name__ == '__main__':
    create_app().run()
