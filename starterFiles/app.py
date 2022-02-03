import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"

@app.route("/")
def index():
    return "<h1>This is My Starter App</h1>"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()