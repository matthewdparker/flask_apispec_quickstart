import os
import sys
import json
import uuid
import logging
import requests
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, fields, marshal_with

from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.schemas import (
	AuthorizationHeaderSchema,
	HealthcheckResponseSchema,
)
from app.utils import (
	marshal_null_return,
	authenticate_request,
	check_entitlements,
	limit_content_length
)


# ---- Resource Definitions ---- #

class HealthcheckAPI(MethodResource, Resource):
	@doc(description='Healthcheck API', tags=['Healthcheck'])
	@authenticate_request
	@limit_content_length()
	@use_kwargs(AuthorizationHeaderSchema, location=('headers'))
	@marshal_with(HealthcheckResponseSchema, description='Success', code=200)
	@marshal_null_return(401, 'Request unauthorized')
	@marshal_null_return(422, 'Unprocessable entity')
	def get(self, Authorization=None):
		"""
		Get method for application healthchecks
		"""
		status = 'healthy'
		return {'status': status}
