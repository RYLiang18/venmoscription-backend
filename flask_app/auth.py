from flask import Blueprint, jsonify, url_for, redirect
from flask_app import oauth
from flask_app.models import User
from flask_login import login_user, login_required, logout_user, current_user

"""
Google Oauth resources:
- https://docs.authlib.org/en/latest/client/flask.html#flask-client
- https://github.com/authlib/demo-oauth-client/blob/master/flask-google-login/app.py
- https://connect2id.com/learn/openid-connect
"""


auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/")
def home():
    return jsonify({"index": "homepage"})


@auth_blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return jsonify(
            {"error": "Forbidden", "message": "You are already authenticated"}
        )
    redirect_uri = url_for("auth.login_auth", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@auth_blueprint.route("/register")
def register():
    if current_user.is_authenticated:
        return jsonify(
            {"error": "Forbidden", "message": "You are already authenticated"}
        )
    redirect_uri = url_for("auth.register_auth", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@auth_blueprint.route("/register-auth")
def register_auth():
    token = oauth.google.authorize_access_token()
    user_info = token["userinfo"]

    # https://connect2id.com/learn/openid-connect
    # Google oauth uses OIDC, `sub` key can be used as ID
    email = user_info["email"]
    subject = user_info["sub"]
    user = User.get(subject)
    if user:
        return jsonify({"error": "Forbidden", "message": f"{email} already exists"})

    User.create(subject, email)
    return ""


# google auth route
@auth_blueprint.route("/login-auth")
def login_auth():
    token = oauth.google.authorize_access_token()
    user_info = token["userinfo"]

    # https://connect2id.com/learn/openid-connect
    # Google oauth uses OIDC, `sub` key can be used as ID
    email = user_info["email"]
    subject = user_info["sub"]
    user = User.get(subject)

    if not user:
        return jsonify({"error": "not found", "message": f"{email} not found"})

    login_user(user)
    return jsonify(user_info)


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
