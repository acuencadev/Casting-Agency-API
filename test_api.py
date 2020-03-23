import json
import pytest

from api import create_app
from api.extensions import db
from api.models import Actor, Movie


@pytest.fixture
def client():
    test_config = {
        'SQLALCHEMY_DATABASE_URI': "sqlite:///test_db.db",
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

    app = create_app(test_config)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()

        yield client


def test_home_route(client):
    response = client.get('/')
    response_json = json.loads(response.data)

    assert 'message' in response_json
    assert "Hello World" == response_json['message']
