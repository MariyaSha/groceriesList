import sys
import sqlite3
from flask import Flask, session, render_template, request
from flask import g
import random

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/", methods = ['POST','GET'])
def main():
    session["all_vals"], session["main_vals"] = get_db()

    return render_template("index.html", 
                            list_options = session["all_vals"], 
                            list_items = session["main_vals"])


@app.route("/remove_items", methods = ['POST'])
def remove_items():
    # get all checked checkbox elements
    checked_boxes = request.form.getlist('check')

    print("detected checked items:", file=sys.stdout)
    for i in checked_boxes:
        print(i, file = sys.stdout)

        if i in session["main_vals"]:
            #remove item & update session
            idx = session["main_vals"].index(i)
            session["main_vals"].pop(idx)
            session.modified = True

    return render_template("index.html", 
                            list_options=session["all_vals"], 
                            list_items=session["main_vals"])


@app.route("/add_item", methods=['POST'])
def add_item():

    session["main_vals"].append(request.form["add_items"])
    session.modified = True

    return render_template("index.html",
                            list_options=session["all_vals"], 
                            list_items=session["main_vals"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')

        cursor = db.cursor()
        cursor.execute("select name from groceries")

        all_vals = cursor.fetchall()
        for i in all_vals:
            print(i, file=sys.stdout)

        # create a list of all items (comes sorted from DB)
        all_vals = [str(val).replace("('", '').replace("',)", '') for val in all_vals]

        # randomly shuffle list and select 5 items
        main_vals = all_vals.copy()
        random.shuffle(main_vals)
        main_vals = main_vals[:5]

    return all_vals, main_vals

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
