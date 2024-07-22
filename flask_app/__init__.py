from flask import Flask
from flask_login import LoginManager
import os
from db import Database


class Config:
    GOOGLE_OAUTH_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )


class DevelopmentConfig(Config):
    DEBUG = True
    SQLITE_DB_LOCATION = "database.db"


database = Database()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)

    database.init_app(app)
    login_manager.init_app(app)

    config_map = {"development": DevelopmentConfig}
    app.config.from_object(config_map[config_name])

    from flask_app.auth import auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app
