from flask import Blueprint, jsonify


movies_bp = Blueprint('movies_bp', __name__)


@movies_bp.route('', methods=['GET'])
def get_all_movies():
    movies = []

    return jsonify({
        'success': True,
        'movies': movies,
        'movies_count': len(movies)
    })
