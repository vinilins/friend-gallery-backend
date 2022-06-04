from flask import Flask
from flask_jwt_extended import JWTManager
from os import getenv

from src.config import config_by_name
from src.photo.controllers import s3_init_app
from src.infra.config.db_config import db_init_app
from src.resources import resources_init_app


def create_app(config_name="production"):

    app = Flask(__name__)
    environment = getenv("FLASK_ENVIRONMENT", config_name)

    app.config.from_object(config_by_name[environment])

    s3_init_app(app)
    db_init_app(app)
    resources_init_app(app)
    JWTManager(app)

    return app
