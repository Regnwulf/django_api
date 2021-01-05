# Django API

Customer's registration Django Restful API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Let's start!

### Prerequisites

Virtualenv

PostgreSQL's Database named "registration_api"

Setup DATABASES on ./registration/settings.py with your local PostgreSQL config.

All the application requisites are on requirements.txt root folder

### Installing

mkdir django_api

cd django_api

pip install virtualenv

python -m venv venv

git clone https://github.com/Regnwulf/django_api.git

To activate venv on Windows:
\path\to\env\Scripts\activate

To activate venv on Linux:
source venv/bin/activate

pip install -r requirements.txt

### Running Server

python manage.py runserver

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs
* [Psycopg](https://www.psycopg.org/docs/) - PostgreSQL database adapter for Python
* [PostgreSQL](https://www.postgresql.org/docs/) - PostgreSQL database

