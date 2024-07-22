from flask_login import UserMixin
from flask_app import login_manager

from db import get_db


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(UserMixin):
    def __init__(self, id_, email):
        self.id = id_
        self.email = email

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        if not user:
            return None

        user = User(id_=user[0], email=user[1])
        return user

    @staticmethod
    def create(id_, email):
        db = get_db()
        db.execute(
            "INSERT INTO user (id, email) VALUES (?, ?)",
            (id_, email),
        )
        db.commit()
