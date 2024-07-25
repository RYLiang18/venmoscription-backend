from flask import Flask
from flask_login import LoginManager
import os
from flask_app.db import Database
from authlib.integrations.flask_client import OAuth


class Config:
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )
    SECRET_KEY = "!secret"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLITE_DB_LOCATION = "database.db"


database = Database()
login_manager = LoginManager()
oauth = OAuth()


def create_app(config_name):
    app = Flask(__name__)

    database.init_app(app)
    login_manager.init_app(app)
    oauth.init_app(app)

    config_map = {"development": DevelopmentConfig}
    app.config.from_object(config_map[config_name])

    oauth.register(
        name="google",
        server_metadata_url=app.config["GOOGLE_DISCOVERY_URL"],
        client_kwargs={"scope": "openid email profile"},
    )

    from flask_app.auth import auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app
