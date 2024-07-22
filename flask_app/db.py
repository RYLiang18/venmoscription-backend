from flask import g, current_app, Flask
import sqlite3


# Database class is a flask extension
# https://flask.palletsprojects.com/en/2.3.x/extensiondev/
# How does init_app(app) work?
# https://stackoverflow.com/questions/19750060/how-to-properly-initialise-the-flask-sqlalchemy-module
class Database:
    def get_db(self) -> sqlite3.Connection:
        if "db" not in g:
            g.db = sqlite3.connect(
                current_app.config["SQLITE_DB_LOCATION"],
                detect_types=sqlite3.PARSE_DECLTYPES,
            )
            g.db.row_factory = sqlite3.Row
        return g.db

    # below link explains why exception parameter AKA 'e' is needed
    # https://stackoverflow.com/questions/57455431/flask-official-tutorial-what-is-e-in-close-dbe-none
    def close_db(self, exception):
        db = g.pop("db", None)

        if db is not None:
            db.close()

    def init_app(self, app: Flask):
        app.teardown_appcontext(self.close_db)
