import sqlite3
import csv

#opening the connection to the database
DATABASE = "netflix_dbase.db"
connection =sqlite3.connect(DATABASE)
cursor = connection.cursor()

#removing tables if they exist when we need to update the database
connection.execute("DROP TABLE IF EXISTS movie")
connection.execute("DROP TABLE IF EXISTS ratings")
connection.execute("DROP TABLE IF EXISTS users")

print("Tables dropped successfully")
#Create three tables(users, movie and ratings)
connection.execute("CREATE TABLE movie(\
    MOVIE_ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    MOVIE_TITLE TEXT,\
    DIRECTOR TEXT,\
    CAST TEXT,\
    COUNTRY INTEGER,\
    RELEASE_YEAR DATETIME,\
    DESCRIPTION TEXT,\
    GENRE TEXT,\
    TYPE TEXT,\
    TV_RATING TEXT)")


connection.execute("CREATE TABLE ratings(\
    MOVIE_ID INTEGER,\
    RATING FLOAT,\
    NUMBER_OF_VOTES INTEGER,\
    YEAR_ADDED DATETIME,\
    FOREIGN KEY(MOVIE_ID) REFERENCES movie(MOVIE_ID))")

connection.execute("CREATE TABLE users(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    FIRSTNAME TEXT,\
    LASTNAME TEXT,\
    EMAIL TEXT,\
    PASSWORD TEXT,\
    FAVORITE_GENRE TEXT,\
    MOVIE_ID INTEGER,\
    FOREIGN KEY(MOVIE_ID) REFERENCES movie(MOVIE_ID))")

print("tables created successfully")