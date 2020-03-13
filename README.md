# Kea Database
An online database designed to track kata information
Kata-back
================

Setup
-----
This guide assumes that `python3`, `pip`, `postgres` (with postgis) and virtual environments are installed.

For instructions on setting up PostGIS:
<https://docs.djangoproject.com/en/1.10/ref/contrib/gis/install/postgis/>

1. Setup `python3` virtual environment
2. Create a new database 'kata' with username/password 'kata'/'kata'
3. `pip install -r requirements.txt`
4. `./manage.py migrate`
5. `./manage.py createsuperuser`

Running
-------
`./manage.py runserver`
