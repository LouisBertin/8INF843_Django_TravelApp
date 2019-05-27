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

* :warning: duplicate `./project/settings.py.env` and rename it `settings.py`. And add your database credentials inside!
* To have the latest database version, don't forget to run this command line : `docker-compose run web python manage.py migrate`

## How to use Django CLI

* You need to run your command line with docker : `docker-compose run web YOUR_DJANGO_COMMAND`