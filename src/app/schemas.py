from flask_restful import fields
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, validate


# ---- Authorization Header ---- #

class AuthorizationHeaderSchema(Schema):
	Authorization = fields.String(description="All PeopleReign Conversation API requests require an Authorization header which includes a bearer token provided by PeopleReign. The value for the Authorization header should be like: 'Bearer <bearer_token>'")


# ---- Healthcheck ---- #

class HealthcheckResponseSchema(Schema):
	status = fields.String(default='healthy',
						   description="The health status of the API",
						   validate=validate.OneOf([
								"healthy",
								"unhealthy"]))
