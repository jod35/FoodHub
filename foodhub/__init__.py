from flask import Flask
from .utils.database import db


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    return app
