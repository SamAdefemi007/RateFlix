import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

DATABASE = "netflix_dbase.db"

def connect_db_row():
    global connection, cursor
    connection = sqlite3.connect(DATABASE)
    connection.row_factory =sqlite3.Row
    cursor=connection.cursor()

@app.route('/')
def index():  # put application's code here
    connect_db_row()
    cursor.execute("Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID LIMIT 10")
    rows = cursor.fetchall()
    connection.close()
    return render_template('index.html', rows=rows)