import json
from dateutil import parser

from flask import abort, Blueprint, jsonify, request

from ..api_service import MoviesRepository
from ..auth import requires_auth


MOVIES_PER_PAGE = 10

movies_bp = Blueprint('movies_bp', __name__)


@movies_bp.route('', methods=['GET'])
@requires_auth('get:movies')
def get_all_movies(jwt):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * MOVIES_PER_PAGE
    end = start + MOVIES_PER_PAGE

    movies = MoviesRepository.get_all_movies()

    return jsonify({
        'success': True,
        'movies': movies[start:end],
        'movies_count': len(movies)
    })


@movies_bp.route('/<int:movie_id>', methods=['GET'])
@requires_auth('get:movie')
def get_movie_by_id(jwt, movie_id):
    movie = MoviesRepository.get_movie_by_id(movie_id)

    if not movie:
        abort(404)

    return jsonify({
        'success': True,
        'movie': movie
    })


@movies_bp.route('', methods=['POST'])
@requires_auth('post:movie')
def create_movie(jwt):
    data = request.get_json()

    if 'title' not in data or 'release_date' not in data:
        abort(400)

    movie = MoviesRepository.create_movie(
        title=data['title'], release_date=parser.parse(data['release_date']))

    if not movie:
        abort(400)

    return jsonify({
        'success': True,
        'movie': movie
    })


@movies_bp.route('/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movie')
def update_movie(jwt, movie_id):
    data = request.get_json()

    if 'title' not in data:
        abort(400)

    release_date = parser.parse(
        data['release_date']) if 'release_date' in data else None

    movie = MoviesRepository.update_movie(
        movie_id, title=data['title'],
        release_date=release_date)

    if not movie:
        abort(404)

    return jsonify({
        'success': True,
        'movie': movie
    })


@movies_bp.route('<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_movie(jwt, movie_id):
    movie = MoviesRepository.get_movie_by_id(movie_id)

    if not movie:
        abort(404)

    deleted = MoviesRepository.delete_movie(movie_id)

    if not deleted:
        abort(500)

    return jsonify({
        'success': True,
        'delete': movie_id
    })


@movies_bp.route('<int:movie_id>', methods=['POST'])
@requires_auth('post:assign-actor')
def assign_actor(jwt, movie_id):
    movie = MoviesRepository.get_movie_by_id(movie_id)

    if not movie:
        abort(404)

    data = request.get_json()

    if 'actor_id' not in data:
        abort(400)

    actor_id = data['actor_id']

    if not MoviesRepository.assign_actor(movie_id, actor_id):
        abort(400)

    return jsonify({
        'success': True
    })
