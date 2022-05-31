from flask import Flask
from flask_jwt_extended import JWTManager
from os import getenv
from src.auth.resources import login_routes
from src.infra.config.db_config import DBConnectionHandler
from src.photo.resources import photo_routes
from src.user.resources import user_routes


app = Flask(__name__)

db_connection = DBConnectionHandler()
db_connection.get_db_engine()

app.config["JWT_SECRET_KEY"] = getenv("AUTHENTICATION_TOKEN_PASSWORD")
app.config["JWT_ALGORITHM"] = "HS256"
app.config["JWT_IDENTITY_CLAIM"] = "sub"

jwt = JWTManager(app)

app.register_blueprint(user_routes)
app.register_blueprint(login_routes)
app.register_blueprint(photo_routes)
