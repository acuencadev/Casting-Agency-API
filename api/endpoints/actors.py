import json
from dateutil import parser

from flask import abort, Blueprint, jsonify, request

from ..api_service import ActorsRepository
from ..auth import requires_auth


ACTORS_PER_PAGE = 10

actors_bp = Blueprint('actors_bp', __name__)


@actors_bp.route('', methods=['GET'])
@requires_auth('get:actors')
def get_all_actors():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ACTORS_PER_PAGE
    end = start + ACTORS_PER_PAGE

    actors = ActorsRepository.get_all_actors()

    return jsonify({
        'success': True,
        'actors': actors[start:end],
        'actors_count': len(actors)
    })


@actors_bp.route('/<int:actor_id>', methods=['GET'])
@requires_auth('get:actor')
def get_actor_by_id(actor_id):
    actor = ActorsRepository.get_actor_by_id(actor_id)

    if not actor:
        abort(404)

    return jsonify({
        'success': True,
        'actor': actor
    })


@actors_bp.route('', methods=['POST'])
@requires_auth('post:actor')
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
@requires_auth('patch:actor')
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


@actors_bp.route('<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(actor_id):
    actor = ActorsRepository.get_actor_by_id(actor_id)

    if not actor:
        abort(404)

    deleted = ActorsRepository.delete_actor(actor_id)

    if not deleted:
        abort(500)

    return jsonify({
        'success': True,
        'delete': actor_id
    })
