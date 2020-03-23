from flask import Flask, jsonify


def create_app(test_settings=None):
    app = Flask(__name__)
    app.config.from_object('api.config.Config')

    if test_settings:
        app.config.update(test_settings)

    register_extensions(app)
    register_blueprints(app)

    @app.route('/')
    def home():
        return jsonify({
            'message': "Hello World"
        })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': "Unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': "Forbidden"
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "Unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "Internal error"
        }), 500

    return app


def register_extensions(app: Flask):
    from .extensions import cors, db, migrate
    from .models import Movie, Actor

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app: Flask):
    from .endpoints import actors_bp, movies_bp

    app.register_blueprint(actors_bp, url_prefix='/actors')
    app.register_blueprint(movies_bp, url_prefix='/movies')
