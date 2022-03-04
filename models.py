import sqlite3
import csv
import sys

DATABASE = "netflix_dbase.db"
#opening the connection to the database      
try:
    connection =sqlite3.connect(DATABASE)
    cursor = connection.cursor()
except:
    print("Connection error, cannot connect to the database, check to see that sqlite3 is imported and that the database path is correct")
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

#loading the open data into the rows in our database

try:
    file = open("open_data/clean_df1.csv",mode="r", newline="")
except OSError:
    print(f"Could not open file ")
    sys.exit()
except FileNotFoundError:
    print(f"No such file or directory : {file}")

try:
    with file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        for row in reader:
            MOVIE_ID = row[0]
            MOVIE_TITLE = row[1]
            DIRECTOR = row[2]
            CAST = row[3]
            COUNTRY = row[4]
            RELEASE_DATE =row[5]
            DESCRIPTION= row[8]
            GENRE = row[13]
            RATING = float(row[14])
            NUMBER_OF_VOTES= int(row[15])
            YEAR_ADDED = row[16]
            TYPE= row[9]
            TV_RATING = row[6]
            cursor.execute('INSERT INTO movie VALUES (?,?,?,?,?,?,?,?,?,?)', (MOVIE_ID, MOVIE_TITLE,DIRECTOR,CAST,COUNTRY,RELEASE_DATE,DESCRIPTION,GENRE, TYPE, TV_RATING))
            cursor.execute('INSERT INTO ratings VALUES (?,?,?,?)',(MOVIE_ID,RATING, NUMBER_OF_VOTES, YEAR_ADDED))
            connection.commit()
        connection.close()
    file.close()
    print("data parsed successfully")

except SyntaxError as error:
    print(f"Please check that you are using the correct SQL commands, {error}")


