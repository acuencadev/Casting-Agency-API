from flask import abort, Blueprint, current_app, jsonify, request

from ..auth import requires_auth


base_bp = Blueprint('base_bp', __name__)


@base_bp.route('/', methods=['GET'])
def home():
    return jsonify({
        'version': current_app.config['API_VERSION']
    })


@base_bp.route('/login_results', methods=['GET'])
@requires_auth('get:login_results')
def login_results(jwt):
    token = request.args.get('access_token', None)

    if not token:
        abort(403)

    return jsonify({
        'message': "You are logged in now!",
        'token': token
    })
