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


def test_get_all_movies_returns_ok(client):
    response = client.get('/movies')
    response_json = json.loads(response.data)

    assert response_json['success'] == True
    assert response_json['movies'] == []
    assert response_json['movies_count'] == 0


def test_get_non_existing_movie_returns_ok_but_empty_response(client):
    response = client.get('/movies/0')
    response_json = json.loads(response.data)

    assert 404 == response.status_code
