# To Do:

## Documentation

- Resolve issue with how flask-apispec and marshmallow are auto-generating swaggerfile; some combination of custom-decorators, wrapping marshal_with, etc. mean the auto-generated docs don't populate request parameters, headers, or response codes as written/expected.

- Integrate with [python-dotenv](https://pypi.org/project/python-dotenv/) to accept environment variables

- Extend testing infrastructure to utilize [tox](https://tox.readthedocs.io/en/latest/) for testing package-version compatibility, etc.

- Build an integration to a default, pre-populated sqlite and/or Postgres database for convenience.

- Write Dockerfile

- Write docker-compose.yml to bring up a network containing app, Postgres, etc.
