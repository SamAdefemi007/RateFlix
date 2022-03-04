import sqlite3
from flask import Flask, render_template


app = Flask(__name__)
DATABASE = "netflix_dbase.db"

def connect_db():
    global connection, cursor
    connection = sqlite3.connect(DATABASE)
    connection.row_factory =sqlite3.Row
    cursor=connection.cursor()

@app.route("/")
def index():
    connect_db()
    cursor.execute("Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID LIMIT 10")
    rows = cursor.fetchall()
    connection.close()
    return render_template('index.html', rows=rows)

@app.route('/movies')
def movies():
    connect_db()
    if session.get("logged_in"):
        cursor.execute("Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID AND movie.TYPE=\"movie\" ORDER BY ratings.RATING DESC")
    else:
        cursor.execute(
            "Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID AND movie.TYPE=\"movie\" ORDER BY ratings.RATING DESC LIMIT 10")
    rows = cursor.fetchall()
    connection.close()

    return render_template('movies.html', rows=rows)


@app.route('/tvshows')
def tvshows():
    connect_db()
    if session.get("logged_in"):
        cursor.execute("Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID AND movie.TYPE!=\"movie\" ORDER BY ratings.RATING DESC")
    else:
        cursor.execute(
            "Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID AND movie.TYPE!=\"movie\" ORDER BY ratings.RATING DESC LIMIT 10")
    rows = cursor.fetchall()
    connection.close()

    return render_template('tvshows.html', rows=rows)

if __name__ == "__main__":
    app.run(debug=True)