from flask import abort, Blueprint, jsonify

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


@actors_bp.route('/<int:actor_id>', methods=['GET'])
def get_actor_by_id(actor_id):
    actor = ActorsRepository.get_actor_by_id(actor_id)

    if not actor:
        abort(404)

    return jsonify({
        'success': True,
        'actor': actor
    })
