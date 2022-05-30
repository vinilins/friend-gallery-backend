from flask import Flask
from flask_jwt_extended import JWTManager
from src.auth.resources import login_routes
from src.infra.config.db_config import DBConnectionHandler
from src.photo.resources import photo_routes
from src.user.resources import user_routes


app = Flask(__name__)

db_connection = DBConnectionHandler()
db_connection.get_db_engine()

jwt = JWTManager(app)

app.register_blueprint(user_routes)
app.register_blueprint(login_routes)
app.register_blueprint(photo_routes)
