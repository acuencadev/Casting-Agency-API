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

            keanu_reeves = Actor(name="Keanu Reeves", age=55, gender="M")

            db.session.add(the_matrix)
            db.session.add(keanu_reeves)
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


def test_get_existing_movie_returns_ok(client):
    response = client.get('/movies/1')
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert 'movie' in response_json


def test_create_movie_without_params_returns_bad_request(client):
    response = client.post('/movies', json={})

    assert 400 == response.status_code


def test_create_movie_with_params_return_ok(client):
    response = client.post('/movies', json={
        'title': "Gladiator",
        'release_date': '2000-05-05'
    })
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert 'Gladiator' == response_json['movie']['title']


def test_update_movie_without_params_returns_bad_request(client):
    response = client.patch('/movies/0', json={})

    assert 400 == response.status_code


def test_update_non_existing_movie_returns_not_found(client):
    response = client.patch('/movies/0', json={
        'title': "The Matrix Reloaded"
    })

    assert 404 == response.status_code


def test_update_existing_movie_returns_ok(client):
    response = client.patch('/movies/1', json={
        'title': "The Matrix Reloaded"
    })
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert "The Matrix Reloaded" == response_json['movie']['title']


def test_delete_non_existing_movie_returns_not_found(client):
    response = client.delete('/movies/0')

    assert 404 == response.status_code


def test_delete_existing_movie_returns_ok(client):
    response = client.delete('/movies/1')
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert 1 == response_json['delete']


def test_get_all_actors_returns_ok(client):
    response = client.get('/actors')
    response_json = json.loads(response.data)

    assert response_json['success'] == True
    assert response_json['actors_count'] == 1


def test_get_non_existing_actor_returns_not_found(client):
    response = client.get('/actors/0')
    response_json = json.loads(response.data)

    assert 404 == response.status_code


def test_get_existing_actor_returns_ok(client):
    response = client.get('/actors/1')
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert 'actor' in response_json


def test_create_actor_without_params_returns_bad_request(client):
    response = client.post('/actors', json={})

    assert 400 == response.status_code


def test_create_actor_with_params_return_ok(client):
    response = client.post('/actors', json={
        'name': "Russell Crowe",
        'age': 60,
        'gender': "M"
    })
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert 'Russell Crowe' == response_json['actor']['name']


def test_update_actor_without_params_returns_bad_request(client):
    response = client.patch('/actors/0', json={})

    assert 400 == response.status_code


def test_update_non_existing_actor_returns_not_found(client):
    response = client.patch('/actors/0', json={
        'name': "Ben Stiller",
        'age': 42,
        'gender': "M"
    })

    assert 404 == response.status_code


def test_update_existing_actor_returns_ok(client):
    response = client.patch('/actors/1', json={
        'name': "Ben Stiller",
        'age': 42,
        'gender': "M"
    })
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert "Ben Stiller" == response_json['actor']['name']


def test_delete_non_existing_actor_returns_not_found(client):
    response = client.delete('/actors/0')

    assert 404 == response.status_code


def test_delete_existing_movie_returns_ok(client):
    response = client.delete('/actors/1')
    response_json = json.loads(response.data)

    assert 200 == response.status_code
    assert 1 == response_json['delete']
