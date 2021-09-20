import functools
from flask import request, abort
from flask_apispec import marshal_with


def marshal_null_return(code, description):
	"""
	API request method decorator to simplify marshalling code when returning None. Cuts down on boilerplate code.

	:type code: Integer
	:param code: HTTP status code to marshal
	:type description: String
	:param description: Description of when and why the marshalled status-code will be returned.
	"""
	return marshal_with(schema=None,
						code=code,
						description=description,
						apply=False)


def authenticate_request(func):
	"""
	API request method decorator to perform request authentication, if required.
	"""
	def wrapper(*args, **kwargs):
		# Implement any required authentication here

		res = func(*args, **kwargs)
		return res

	return wrapper


def check_entitlements(required_entitlements=[]):
	"""
	API request method decorator to check entitlements, if enforcing any.
	"""
	def decorator_func(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			# Implement any entitlements-checking here
			if True:
				pass

			else:
				abort(403, 'Entitlements exceeded')
			return func(*args, **kwargs)
		return wrapper
	return decorator_func


def limit_content_length(max_length=10000):
	"""
	API request method decorator to limit the request content-length for security purposes.
	"""
	def decorator_func(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			cl = request.content_length
			if cl is not None and cl > max_length:
				abort(400, 'Request exceeded maximum content-length')

			return func(*args, **kwargs)
		return wrapper
	return decorator_func
