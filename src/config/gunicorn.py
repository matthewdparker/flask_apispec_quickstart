import os
from dotenv import dotenv_values

env_config = {
	**dotenv_values(".env.shared"),  # load shared development variables
	**dotenv_values(".env.secret"),  # load sensitive variables
	**os.environ,  # override loaded values with environment variables
}


"""
See https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py for a fully-annotated sample Gunicorn config file.
"""


bind = '0.0.0.0:' + str(env_config.get('GUNICORN_PORT', '5000'))
timeout = int(env_config.get('GUNICORN_TIMEOUT', 60))  # seconds
cpus = int(env_config.get('GUNICORN_CPUS', 1))
workers = int(env_config.get('GUNICORN_WORKERS', 1))
backlog = 2048
errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
