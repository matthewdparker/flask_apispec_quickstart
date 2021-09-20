from src.app.main import make_app


@pytest.fixture
def client():
	app = make_app({'TESTING': True})
	with app.test_client() as client:
		yield client


def test_limit_content_length(client):
	url = '/healthcheck'
	rv = client.get(url, json={'data': 'aaaaa'*10000000})
	assert(rv.status_code == 400)
