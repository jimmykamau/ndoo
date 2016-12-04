[![Build Status](https://travis-ci.org/andela-jkamau/ndoo.svg?branch=development)](https://travis-ci.org/andela-jkamau/ndoo)
[![Coverage Status](https://coveralls.io/repos/github/andela-jkamau/ndoo/badge.svg?branch=master)](https://coveralls.io/github/andela-jkamau/ndoo?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ad46f1a131094f7dad0d30d10b2a1404)](https://www.codacy.com/app/jimmy-kamau/ndoo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-jkamau/ndoo&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/andela-jkamau/ndoo/master/landscape.svg?style=flat)](https://landscape.io/github/andela-jkamau/ndoo/master)
![alt text](https://img.shields.io/badge/python-2.7-blue.svg)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)


# Ndoo
Ndoo is a bucket list service built in Python/Django and jQuery.

## Installation and setup
Clone this repo:
```
$ https://github.com/andela-jkamau/ndoo
```


Navigate to the `ndoo` directory:
```
$ cd ndoo
```

Create a virtual environment and activate it using [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Install dependancies:
```
$ pip install -r requirements.txt
```
Add `SECRET_KEY`, `PATH`, `DB_USER`, `DB_PASS` and `DB_PATH` to your environment variables
```
export SECRET_KEY='reallysecret'
export PATH=$PATH:PATH_TO_NDOO
export DB_USER='username'
export DB_PASS='password'
export DB_PATH='PATH_TO_DB'
```

Migrate and upgrade the database:
```
python manage.py makemigrations
python manage.py migrate
```

Run tests to ensure everything is working as expected:
~~~
$ python manage.py test
~~~

## Usage

To start the app:

` python run.py runserver `

Access the endpoints using your preferred client e.g Postman

### API Endpoints

| Resource URL | Methods | Description | Requires Token |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/auth/register` | POST  | User registration | FALSE |
| `/api/v1/auth/login` | POST | User login | FALSE |
| `/api/v1//bucketlists/` | GET, POST | A user's bucket lists | TRUE |
| `/api/v1/bucketlists/<id>` | GET, PUT, DELETE | A single bucket list | TRUE |
| `/api/v1/bucketlists/<id>/items` | GET, POST | Items in a bucket list | TRUE |
| `/api/v1/bucketlists/<id>/items/<item_id>` | GET, PUT, DELETE | A single bucket list item | TRUE |
| `/docs` | - | A single bucket list item | FALSE |

| Method | Description |
|------- | ----------- |
| GET | Retrieves a resource(s) |
| POST | Creates a new resource |
| PUT | Updates an existing resource |
| DELETE | Deletes an existing resource |

### Web URL

|  URL |  Description |
| -------- | ------------- |
| `/` |  Index page can Login and Sign Up|
| `/dashboard` | Bucketlist operations |
