import os
from flask import Flask
# Load environment variables from a .env file when available
try:
    # python-dotenv is optional in requirements; if present load it
    from dotenv import load_dotenv
    # load variables from .env at the project root (flask_app/.env)
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
except Exception:
    # If python-dotenv isn't installed or load fails, continue using OS env
    pass


def create_app():
    # templates/static are located in ../main (same structure as your Django app)
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_folder = os.path.join(root, '..', 'main', 'templates')
    static_folder = os.path.join(root, '..', 'main', 'static')

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')

    # register routes
    from .routes import bp
    app.register_blueprint(bp)

    return app
