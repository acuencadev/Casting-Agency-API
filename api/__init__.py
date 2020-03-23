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

    return app


def register_extensions(app: Flask):
    from api.extensions import db, migrate
    from api.models import Movie, Actor

    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app: Flask):
    from .endpoints import actors_bp, movies_bp

    app.register_blueprint(actors_bp)
    app.register_blueprint(movies_bp)
