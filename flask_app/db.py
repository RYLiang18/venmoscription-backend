from flask import g, current_app
import sqlite3, os


def get_db() -> sqlite3.Connection:
    print("CURRENT APP sqlite location", type(current_app.config["SQLITE_DB_LOCATION"]))
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["SQLITE_DB_LOCATION"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
    return g.db
