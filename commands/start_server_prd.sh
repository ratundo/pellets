#!/bin/bash

pipenv run python src/manage.py migrate
pipenv run python src/manage.py collectstatic --noinput
pipenv run python src/manage.py runserver 0.0.0.0:8010