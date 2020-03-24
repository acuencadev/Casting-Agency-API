import json
from dateutil import parser

from flask import abort, Blueprint, jsonify, request

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


@actors_bp.route('', methods=['POST'])
def create_actor():
    data = request.get_json()

    if 'name' not in data or 'age' not in data or 'gender' not in data:
        abort(400)

    actor = ActorsRepository.create_actor(
        name=data['name'], age=data['age'], gender=data['gender'])

    if not actor:
        abort(400)

    return jsonify({
        'success': True,
        'actor': actor
    })


@actors_bp.route('/<int:actor_id>', methods=['PATCH'])
def update_actor(actor_id):
    data = request.get_json()

    if 'name' not in data and 'age' not in data and 'gender' not in data:
        abort(400)

    name = data['name'] if 'name' in data else None
    age = data['age'] if 'age' in data else None
    gender = data['gender'] if 'gender' in data else None

    actor = ActorsRepository.update_actor(
        actor_id, name=name, age=age, gender=gender)

    if not actor:
        abort(404)

    return jsonify({
        'success': True,
        'actor': actor
    })
