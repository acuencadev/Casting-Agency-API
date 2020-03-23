import json
import pytest
from datetime import datetime

from api import create_app
from api.extensions import db
from api.models import Actor, Movie


@pytest.fixture
def client():
    test_config = {
        'SQLALCHEMY_DATABASE_URI': "sqlite:///:memory:",
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

    app = create_app(test_config)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            the_matrix = Movie(title="The Matrix",
                               release_date=datetime(1999, 6, 10))

            db.session.add(the_matrix)
            db.session.commit()

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
    assert response_json['movies_count'] == 1


def test_get_non_existing_movie_returns_not_found(client):
    response = client.get('/movies/0')
    response_json = json.loads(response.data)

    assert 404 == response.status_code


def test_get_non_existing_movie_returns_ok(client):
    response = client.get('/movies/1')
    response_json = json.loads(response.data)

    assert 200 == response.status_code
