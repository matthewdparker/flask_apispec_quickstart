import os
from dotenv import dotenv_values


env_config = {
	**dotenv_values(".env.shared"),  # load shared development variables
	**dotenv_values(".env.secret"),  # load sensitive variables
	**os.environ,  # override loaded values with environment variables
}
