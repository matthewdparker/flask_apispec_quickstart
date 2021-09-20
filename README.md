# Overview
This repo was designed as a simple out-of-the-box app for building custom RESTful APIs. It utilizes marshmallow and flask-apispec for request and response schema definition and automatic Swagger doc-gen.

The repo comes with a simple healthcheck API, and a few decorators which can be customized depending on requirements.

NOTE: Still a few kinks to work out with flask-apispec, there are elements of the API which aren't coming through in the documentation. For more info see TODO.md.


## Requirements

1. Python >= 3.6


## Setup

1. Clone the repo and change working directory to `.../flask_apispec_quickstart`
2. Create and activate a new virtual environment
3. Upgrade pip and install requirements
    >`$ git clone https://github.com/matthewdparker/flask_apispec_quickstart` \
    `$ python -m venv venv` \
    `$ source venv/bin/activate` \
    `$ pip install --upgrade pip` \
    `$ pip install -r requirements.txt`


## Starting the app

### Development
Start a Flask development server on `http://localhost:5000/` with: `$ python src/app/main.py`.

### Production
Start a production Gunicorn server on `http://localhost:5000/` from the `/src/` working directory with: `$ gunicorn --config=src/config/gunicorn.py app.wsgi:app --reload`


## Testing

This repo is set up with a few simple `pytest` tests, and `coverage` for code coverage measurement. Tests are located under `/src/test`. To run tests from the top level directory:

`$ python -m pytest --cov=src/. --cov-config=.coveragerc`

To just get a coverate report from the latest test, do:

`$ coverage report`


## Documentation

Swagger documentation is auto-generated by `flask_apispec` and `marshmallow`. To access the documentation, start the server and navigate to `/swagger` in a browser. To access an interactive Swagger UI, navigate to `/swagger-ui`.
