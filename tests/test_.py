import sqlite3
from rateflix.app import app
from rateflix import models
from pathlib import Path

def test_page_setup():
    #page setup testing as done in TDD development by https://github.com/mjhea0/flaskr-tdd
    tester= app.test_client()
    response = tester.get("/", content_type = "html/text")
    assert response.status_code ==200



def test_db_file():
    assert Path(models.DATABASE).is_file()
    #test passed

def test_db_table_creation():
    connection =sqlite3.connect(models.DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    assert cursor.fetchall() == [("sqlite_sequence",),("movie",),("ratings",),("users",)]
    connection.close()
    #tables created successfully in the database

def test_table_data():
    connection =sqlite3.connect(models.DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) from movie")
    assert cursor.fetchall()==[(4169,)]
    connection.close()
    #all rows in the open_data loaded successfully
    #This particular tests takes about 3-4mins to run

