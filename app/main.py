# /app/__init__.py

import os
import logging
from flask import Flask

#Local imports
import database
from api.base import api_router_v1
from waitress import serve


def create_app():
    """Factory function that creates the Flask app"""

    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)

    # Initialize extensions
    database.init_app(app) # PostgreSQL db with psycopg2
    app.register_blueprint(api_router_v1, url_prefix='/api/v1')

    return app

app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000, threads=10)
