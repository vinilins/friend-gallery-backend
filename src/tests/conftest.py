from os import getenv

import pytest
from flask import Flask
from src.resources import resources_init_app
from src.config import config_by_name
from mongoengine import connect, disconnect
from flask_jwt_extended import JWTManager


@pytest.fixture()
def mock_env(monkeypatch):
    monkeypatch.setenv("JWT_SECRET_KEY", "other-secret-key")
    monkeypatch.setenv("FLASK_ENV", "testing")


@pytest.fixture()
def mongo():
    db = connect("mongoenginetest", host="mongomock://localhost")
    yield db
    db.drop_database("mongoenginetest")
    db.close()
    return


@pytest.fixture()
def app(mongo, mock_env):
    app = Flask(__name__)

    env = getenv("FLASK_ENV")
    app.config.from_object(config_by_name[env])

    resources_init_app(app)
    JWTManager(app)

    with app.app_context():
        yield app

    disconnect()
