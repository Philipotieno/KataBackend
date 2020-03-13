# Kea Database
An online database designed to track kata information
Kata-back
================

Setup
-----
This guide assumes that `python3`, `pip`, `postgres` (with postgis) and virtual environments are installed.

For instructions on setting up PostGIS:
<https://docs.djangoproject.com/en/1.10/ref/contrib/gis/install/postgis/>
```
Create postgres database
 $ sudo su postgres
 $ psql
 postgres=# CREATE USER kata WITH PASSWORD 'password';
 postgres=# ALTER ROLE kata SET client_encoding TO 'utf8';
 postgres=# ALTER ROLE kata SET default_transaction_isolation TO 'read committed';
 postgres=# ALTER ROLE kata SET timezone TO 'UTC';
 postgres=# CREATE DATABASE katadatabse;
 postgres=# GRANT ALL PRIVILEGES ON DATABASE katadatabse TO kata;
 postgres=# \c katadatabe
 katadatabse=# CREATE EXTENSION postgis;
 katadatabse=# \q
 $ exit

 ```

1. Setup `python3` virtual environment
2. Create a new database 'kata' with username/password 'kata'/'kata'
3. `$ pip install -r requirements.txt`
4.  copy .env-example to .env
    - `$ cp .env-example .env`
4. `$ ./manage.py migrate`
5. `$ ./manage.py createsuperuser`

Running
-------
`$ ./manage.py runserver`
