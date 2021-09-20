# sys.path.append(dirname(dirname(abspath(__file__))))
from app.resources import HealthcheckAPI


# ---- Set the application-level configs ---- #
APP_CONFIG = {
	'resources_and_routes' : {
		HealthcheckAPI: '/healthcheck',
	}
}


if __name__ == '__main__':
	pass
