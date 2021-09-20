import pytest
from src.app.main import make_app


@pytest.fixture
def client():
	app = make_app({'TESTING': True})
	with app.test_client() as client:
		yield client


def test_get_healthcheck(client):
	url = '/healthcheck'
	rv = client.get(url)
	assert(rv.status_code == 200)
	assert(rv.json['status'] == 'healthy')
