import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    connection = sqlite3.connect(db_name)
    connection.row_factory =sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID LIMIT 10")
    rows = cursor.fetchall()
    connection.close()
    return render_template('index.html', rows=rows)