from flask import Flask


def create_app():
    app = Flask(__name__)

    from flask_app.auth import auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app
