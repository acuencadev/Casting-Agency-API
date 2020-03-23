import json
from dateutil import parser

from flask import abort, Blueprint, jsonify, request

from ..api_service import MoviesRepository


movies_bp = Blueprint('movies_bp', __name__)


@movies_bp.route('', methods=['GET'])
def get_all_movies():
    movies = MoviesRepository.get_all_movies()

    return jsonify({
        'success': True,
        'movies': movies,
        'movies_count': len(movies)
    })


@movies_bp.route('/<int:movie_id>', methods=['GET'])
def get_movie_by_id(movie_id):
    movie = MoviesRepository.get_movie_by_id(movie_id)

    if not movie:
        abort(404)

    return jsonify({
        'success': True,
        'movie': movie
    })


@movies_bp.route('', methods=['POST'])
def create_movie():
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
