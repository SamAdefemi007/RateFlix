import sqlite3
from flask import Flask, render_template, session, request

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

@app.route('/movies')
def movies():
    connect_db_row()
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
    connect_db_row()
    if session.get("logged_in"):
        cursor.execute("Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID AND movie.TYPE!=\"movie\" ORDER BY ratings.RATING DESC")
    else:
        cursor.execute(
            "Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID AND movie.TYPE!=\"movie\" ORDER BY ratings.RATING DESC LIMIT 10")
    rows = cursor.fetchall()
    connection.close()

    return render_template('tvshows.html', rows=rows)


@app.route('/kidshow')
def kidshow():
    connect_db_row()
    if session.get("logged_in"):
        cursor.execute(
        "Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID WHERE"
        " movie.TV_RATING!=\"NC-17\" AND movie.TV_RATING!=\"NR\" AND movie.TV_RATING!=\"R\" AND movie.TV_RATING!=\"rating\""
        "AND movie.TV_RATING!=\"TV-14\" AND movie.TV_RATING!=\"TV-MA\" AND movie.TV_RATING!=\"UR\" ORDER BY ratings.RATING DESC")
    else:
        cursor.execute(
            "Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID WHERE"
            " movie.TV_RATING!=\"NC-17\" AND movie.TV_RATING!=\"NR\" AND movie.TV_RATING!=\"R\" AND movie.TV_RATING!=\"rating\""
            "AND movie.TV_RATING!=\"TV-14\" AND movie.TV_RATING!=\"TV-MA\" AND movie.TV_RATING!=\"UR\" ORDER BY ratings.RATING DESC LIMIT 10")

    rows = cursor.fetchall()
    connection.close()

    return render_template('kidshow.html', rows=rows)



@app.route('/<query>')
def querysearch(query):
    if query:
        result = request.args.get("search")
        parsed = "%"+ result  +"%"
        connect_db_row()
        cursor.execute("Select * from movie INNER JOIN ratings ON ratings.MOVIE_ID = movie.MOVIE_ID WHERE movie.MOVIE_TITLE Like ? ORDER BY ratings.RATING DESC", (parsed,))
        rows = cursor.fetchall()
        connection.close()

    else:
        return redirect(url_for('/'))

    return render_template('user_search.html', rows=rows, result=result)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=="POST":
            firstname = request.form.get("firstname")
            lastname = request.form.get("lastname")
            email=request.form.get("email")
            genre=  request.form.get("genre")
            password = request.form.get("password")
            connect_db_row()
            cursor.execute("INSERT INTO users VALUES(NULL,?,?,?,?,?, NULL)", (firstname, lastname, email,password, genre))
            connection.commit()
            connection.close()
            session["name"] = firstname
            session["logged_in"]= True
            return redirect(url_for("movies"))
    return render_template("register.html")