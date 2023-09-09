#!/bin/bash

export PYTHONPATH=$(pwd)

cd src/

poetry run python manage.py migrate
poetry run python manage.py importdata ../import-data.csv

poetry run python manage.py runserver 0.0.0.0:8080
