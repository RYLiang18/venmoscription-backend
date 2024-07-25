from flask import Blueprint, jsonify, url_for, redirect
from flask_app import database, oauth
from flask_app.models import User
from flask_login import login_user, login_required, logout_user

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
    redirect_uri = url_for("auth.auth", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


# google auth route
@auth_blueprint.route("/auth")
def auth():
    token = oauth.google.authorize_access_token()
    user_info = token["userinfo"]

    # https://connect2id.com/learn/openid-connect
    # Google oauth uses OIDC, `sub` key can be used as ID
    email = user_info["email"]
    subject = user_info["sub"]
    user = User.get(subject)

    if not user:
        return jsonify({"error": f"{email} user not found"}), 404

    login_user(user)

    return redirect("/")


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
