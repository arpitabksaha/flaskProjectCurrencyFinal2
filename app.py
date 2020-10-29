from flask import *
import sqlite3
import matplotlib.pyplot as plt
import mpld3
import simplejson as json
import pandas as pd


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page_landing():
    if request.method == 'GET':
        con = sqlite3.connect("C:/Users/B K Saha/Downloads/DestinationDB.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from Currency")
        rows = cur.fetchall()
        return render_template('index.html' , rows=rows)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()