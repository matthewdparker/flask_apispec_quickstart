import os
import sys
import uuid
import logging
import requests
from apispec import APISpec
from flask import Flask, request
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import marshal_with, doc, use_kwargs
from marshmallow import Schema, fields, validate, INCLUDE
from flask_restful import Resource, Api, fields, marshal_with

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.app import APP_CONFIG


logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def make_app(test_config=None):
	# Build & configure app, api, and docs instances
	app = Flask(__name__)
	api = Api(app)
	docs = FlaskApiSpec(app)
	app.config.update({
		'APISPEC_SPEC': APISpec(
			title='PeopleReign Conversation API',
			version='2.6.0',
			plugins=[MarshmallowPlugin()],
			openapi_version='3.0.0'
		),
		'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
		'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
	})

	# Add & register resources and routes
	for resource, route in APP_CONFIG['resources_and_routes'].items():
		api.add_resource(resource, route)
		docs.register(resource)

	return app


if __name__ == '__main__':
	app = make_app()
	app.run(debug=True)
