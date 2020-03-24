from flask import Blueprint, jsonify

from ..api_service import ActorsRepository


actors_bp = Blueprint('actors_bp', __name__)


@actors_bp.route('', methods=['GET'])
def get_all_actors():
    actors = ActorsRepository.get_all_actors()

    return jsonify({
        'success': True,
        'actors': actors,
        'actors_count': len(actors)
    })
