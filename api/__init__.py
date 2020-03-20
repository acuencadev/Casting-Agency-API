from flask import Flask, jsonify


def create_app(test_settings=None):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify({
            'message': "Hello World"
        })

    return app
