# To Do:

## Documentation

1. Resolve issue with how flask-apispec and marshmallow are auto-generating swaggerfile; some combination of custom-decorators, wrapping marshal_with, etc. mean the auto-generated docs don't populate request parameters, headers, or response codes as written/expected.

2. Build an integration to a default, pre-populated sqlite and/or Postgres database for convenience.
