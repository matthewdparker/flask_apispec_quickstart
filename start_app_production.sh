#!/bin/bash

gunicorn --config=src/config/gunicorn.py src.app.wsgi:app --reload
