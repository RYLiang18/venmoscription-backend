from flask import Blueprint, jsonify
from flask_app.db import get_db

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/")
def login():
    return jsonify({"hello": "pog"})


@auth_blueprint.route("/adduser", methods=["POST"])
def adduser():
    connection = get_db()
    connection.execute(
        """
        INSERT INTO user (id, email) VALUES (?, ?) 
        """,
        ("user_id", "richard.y.liang@gmail.com"),
    )

    connection.commit()
    connection.close()

    return ""


@auth_blueprint.route("/allusers")
def allusers():
    connection = get_db()
    users = connection.execute(
        """
        SELECT * FROM user
        """
    ).fetchall()
    print(len(users))
    return jsonify({"users": [dict(user) for user in users]})
