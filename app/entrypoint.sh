#!/bin/sh
python3 manage.py collectstatic
python3 manage.py migrate

exec "$@"