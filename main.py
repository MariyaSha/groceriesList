import sys
import sqlite3
from flask import Flask, flash, render_template, request
from flask import g
import random

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# initiallizing global variables
# to beused in multiple methods
all_vals = []
list_vals = []

@app.route("/", methods=['POST','GET'])
def main():
    #access global variables
    global all_vals
    global list_vals

    #load database into global variables
    a_vals, l_vals = get_db()
    all_vals = a_vals.copy()
    list_vals = l_vals.copy()
    print("data is loaded globally", file=sys.stdout)

    return render_template("index.html", list_options=all_vals, list_items=list_vals)

@app.route("/remove_items", methods=['POST'])
def remove_me():
    #access global variables
    global all_vals
    global list_vals

    # get all checked checkbox elements
    checked_items = request.form.getlist('check')
    for i in checked_items:
        print(i, file=sys.stdout)
        # update global variables
        if i in list_vals:
            idx = list_vals.index(i)
            print("found " + i + " at idx: ", idx, file=sys.stdout)
            #remove item
            list_vals.pop(idx)

    return render_template("index.html", list_options=all_vals, list_items=list_vals)

@app.route("/add_item", methods=['POST','GET'])
def test_me():
    #access global variables
    global all_vals
    global list_vals

    list_vals.append(request.form["add_items"])
    print("added " + request.form["add_items"] + " to grocery list", file=sys.stdout)

    return render_template("index.html", list_options=all_vals, list_items=list_vals)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')

        cursor = db.cursor()
        cursor.execute("select name from groceries")

        a_vals = cursor.fetchall()
        a_vals = [str(val).replace("('", '').replace("',)", '') for val in a_vals]
        a_vals = sorted(a_vals)

        m_vals = a_vals.copy()
        m_vals = m_vals[:5]

    return a_vals, m_vals

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
