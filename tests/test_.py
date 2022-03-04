import sqlite3
from rateflix.app import app
from pathlib import Path

DATABASE = "netflix_dbase.db"

def test_page_setup():
    tests= app.test_client()
    response = tests.get("/", content_type = "html/text")
    assert response.status_code ==200



def test_db_file():
    assert Path(DATABASE).is_file()
    #test passed

def test_db_table_creation():
    connection =sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    assert cursor.fetchall() == [("sqlite_sequence",),("movie",),("ratings",),("users",)]
    connection.close()
    #tables created successfully in the database

def test_table_data():
    connection =sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) from movie")
    assert cursor.fetchall()==[(4169,)]
    connection.close()
    #all rows in the open_data loaded successfully
    #This particular tests takes about 3-4mins to run

#testing our page loads without error

def test_movie_page():
    tests= app.test_client()
    response = tests.get("/movies", content_type = "html/text")
    assert response.status_code ==200

def test_tvshow_page():
    tests= app.test_client()
    response = tests.get("/tvshows", content_type = "html/text")
    assert response.status_code ==200

def test_kidshow_page():
    tests= app.test_client()
    response = tests.get("/kidshow", content_type = "html/text")
    assert response.status_code ==200

def test_usersearch_page():
    tests= app.test_client()
    response = tests.get("/user_search", content_type = "html/text")
    assert response.status_code ==200