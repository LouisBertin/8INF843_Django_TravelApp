# 8INF843 Django TravelApp

A Django project

## Setup

* Clone this repository
* Run the following command in the project root directory `docker-compose up`
* That's all!

## Project urls

* Django website : `localhost:8000`
* Adminer : `localhost:8080`

## Database

* To have the latest database version, don't forget to run this command line : `docker-compose run web python manage.py migrate`

## How to use Django CLI

* You need to run your command line with docker : `docker-compose run web YOUR_DJANGO_COMMAND`

## If Docker doesn't work for you :sob: 

* use your own database
* :warning: duplicate `./project/settings.py.env` and rename it `settings.py`. And add your database credentials inside!
* run the python3 server `python manage.py runserver`

## Fixtures

* create new fixture file `python manage.py dumpdata --format=json app > project/fixtures/data.json`
* reset django database `python manage.py flush`
* load fixtures `python manage.py loaddata data`