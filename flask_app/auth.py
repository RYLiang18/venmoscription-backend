from flask import Blueprint, jsonify

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/")
def login():
    return jsonify({"hello": "pog"})
