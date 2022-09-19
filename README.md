# LITReview

This application will allow you to create tickets where you followers can comment and review.
Here the tickets are for asking a review of a book.

## Installation:


1. download & install [python3](https://www.python.org/downloads/)
1. download this repository either by : 
    - terminal: "git clone https://github.com/maximesoydas/maxweb.git" 
    - or by downloading the [zip folder](https://github.com/maximesoydas/maxweb/archive/refs/heads/master.zip)

1. open a terminal and go into the directory where you placed the repository "maxweb"
1. now you will need to enter the virtual environment:
    - type in: "pipenv shell"
1. you then need to install all the dependencies:
    - type in: "pip install -r requirements.py"
1. finally you can run the application:
    - type in: "python manage.py runserver"
1. optional:
    - to empty the db: python manage.py flush
    - to create admin: python manage.py createsuperuser
    - to check PEP8: flake8 .



once the application is launched with the runserver cmd,
you can go to http://127.0.0.1:8000/ and register an account.

you can also access the flake8html result by right clicking on the index.html file in flake-report and select "open with live server" (on vscode... make sure you have the extension live server) 