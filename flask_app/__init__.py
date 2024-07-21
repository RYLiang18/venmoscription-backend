from flask import Flask, g
import os


class Config:
    GOOGLE_OAUTH_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLITE_DB_LOCATION = "database.db"


def create_app(config_name):
    app = Flask(__name__)

    # print("bruh", os.getcwd())

    config_map = {"development": DevelopmentConfig}
    app.config.from_object(config_map[config_name])

    from flask_app.auth import auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app
