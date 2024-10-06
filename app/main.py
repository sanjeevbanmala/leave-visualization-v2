# /app/__init__.py

import os
import logging
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

#Local imports
import database
from os import environ
from api.base import api_router_v1
from waitress import serve

def create_app():
    """Factory function that creates the Flask app"""

    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)

    # Initialize extensions
    #database.init_app(app) # PostgreSQL db with psycopg2
    app.register_blueprint(api_router_v1, url_prefix='/api/v1')
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'  # Path to your Swagger JSON file

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "My API"
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/static/swagger.json')
    def swagger_json():
        return send_from_directory('static', 'swagger.json')

    return app

app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000, threads=10)
