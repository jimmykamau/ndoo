[![Build Status](https://travis-ci.org/andela-landia/adventures.svg?branch=develop)](https://travis-ci.org/andela-landia/adventures)
[![Coverage Status](https://coveralls.io/repos/github/andela-landia/adventures/badge.svg?branch=develop)](https://coveralls.io/github/andela-landia/adventures?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/51601f79615546d289e916cd3817847a)](https://www.codacy.com/app/loice-andia/adventures?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-landia/adventures&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/andela-landia/adventures/develop/landscape.svg?style=flat)](https://landscape.io/github/andela-landia/adventures/develop)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)


# Ndoo
Ndoo is a bucket list service built in Python/Django and jQuery.

## Installation and setup

Clone this repo:

` https://github.com/andela-landia/adventures.git `

Navigate to the `adventures` directory:

` cd adventures `

Create a virtual environment and activate it.

` mkvirtualenv Bucketlist
workon Bucketlist `

Install dependencies:

` pip install -r requirements.txt `

Initialize, migrate and update the database:

` cd adventures `
` python manage.py makemigrations `
` python manage.py migrate `

Test the application by running:

` python manage.py test `

## Usage

To start the app:

` python run.py runserver `

Access the endpoints using your preferred client e.g Postman

### API Endpoints

| Resource URL | Methods | Description | Requires Token |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/register` | POST  | User registration | FALSE |
| `/api/v1/login` | POST | User login | FALSE |
| `/api/v1//bucketlists` | GET, POST | A user's bucket lists | TRUE |
| `/api/v1/bucketlists/<bucketlist_id>` | GET, PUT, DELETE | A single bucket list | TRUE |
| `/api/v1/bucketlists/<bucketlist_id>/items` | GET, POST | Items in a bucket list | TRUE |
| `/api/v1/bucketlists/<bucketlist_id>/items/<item_id>` | GET, PUT, DELETE | A single bucket list item | TRUE |

| Method | Description |
|------- | ----------- |
| GET | Retrieves a resource(s) |
| POST | Creates a new resource |
| PUT | Updates an existing resource |
| DELETE | Deletes an existing resource |

### Web URL

|  URL |  Description |
| -------- | ------------- |
| `/` |  Index page can Login and SignUp|
| `/bucketlists` | User views his list of bucketlists|
| `/onebucketlist` | User views, edits or deletes a single bucketlist and its items |
| `/onebucketlist/<bucketlist_id>/items/<item_id>` |  User views, edits or deletes a single bucket list item|
