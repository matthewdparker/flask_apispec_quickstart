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

# Local imports
from config.environment import env_config
from app.schemas import (
	AuthorizationHeaderSchema,
	HealthcheckResponseSchema,
)
from app.utils import marshal_null_return, limit_content_length


logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


# ---- Resource Definitions ---- #

class HealthcheckAPI(MethodResource, Resource):
	@doc(description='Healthcheck API', tags=['Healthcheck'])
	@limit_content_length()
	@use_kwargs(AuthorizationHeaderSchema, location=('headers'))
	@marshal_with(HealthcheckResponseSchema, description='Success', code=200)
	@marshal_null_return(401, 'Request unauthorized')
	@marshal_null_return(422, 'Unprocessable entity')
	def get(self, Authorization=None):
		"""
		Get method for application healthchecks
		"""
		logger.info("Received /healthcheck request")
		status = 'healthy'
		logger.info(f"Returning status: {status}")
		return {'status': status}
