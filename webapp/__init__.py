from flask import Flask, render_template
# import secrets
import os
# from logging.config import dictConfig
# from . import db as DB
# from .utils import (
#     has_role,
#     format_datetime,
#     format_timedelta,
# )
# from .monitors import Monitor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config.from_object('config_dev')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # Import all routes from blueprints:
    from .views.main import main
    app.register_blueprint(main)

    from .views.auth import auth
    app.register_blueprint(auth)

    return app
