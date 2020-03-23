from flask import abort, Blueprint, jsonify

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
        'movie': {}
    })
