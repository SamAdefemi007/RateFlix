RATEFLIX, @2022

What is Rateflix?

Rateflix is a movie recommendation web application that allows users to search for the best movies on Neflix as voted by IMDB users

Why Rateflix?

The application was developed for the advanced programming course CS551P assessment and i choose this particular dataset because
i wanted to build something personal. I always have a hard time picking good movies on Netflix, so i decided to build a web application that recommends one

How was Rateflix built?
Rateflix was built using the software development process below
-User research: I created a persona(in the root folder of this submission -User persona.pdf ) so i could get the user requirements for this web application
- The web application design template was to use a Model-View-Controller Architecture, The plan was to separate my database(models.py) from my application's logic(app.py) and my View(templates and static)
- The actual creation of the web application was completed using the following steps
    -Initializing the project folder on git with constant commits after each of the steps below
    -installing flask and pytest
    - Creating the database
    -Creating tables in the database(Movies, ratings and users table)
    -Opening the data file containing the open data downloaded from Kaggle
    -Populating the database rows with data
    -Running tests using pytest to check the database path and the number of records in the database
    -Building the user interface using HTML and CSS 
    -Creating the logic that supports the web application in app,py
    - Running more tests to be sure all page loads as intended
    -Deployment on heroku


Maintenace details
 please see below username and password to test the login page
 username: admin@admin.com
 password:admin

Heroku Url:
https://rate-flix.herokuapp.com/


