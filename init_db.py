import sqlite3

connection: sqlite3.Connection = sqlite3.connect("database.db")
with open("schema.sql") as f:
    connection.executescript(f.read())
