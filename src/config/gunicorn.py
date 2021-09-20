import os
import sys
from os.path import dirname, abspath

"""
See https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py for a fully-annotated sample Gunicorn config file.
"""
bind = '0.0.0.0:5000'
timeout = 60  # seconds
cpus = 1
workers = 1
backlog = 2048
errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
