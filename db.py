import sqlite3

import click
from flask import current_app, g #Current_app for session creation and follow up

#this file is used to create connection to the database only and close it by calling these funtions

#connecting to the database
def get_db():
    db = sqlite3.connect('my_db.sqlite',detect_types=sqlite3.PARSE_DECLTYPES) # conneccting to the database
    db.row_factory = sqlite3.Row
    return db

#closing the connection
def close_db(db=None):
    if db is not None:
        db.close()
        