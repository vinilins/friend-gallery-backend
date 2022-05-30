from flask import Flask
from src.infra.config.db_config import DBConnectionHandler
from src.user.resources import user_routes


app = Flask(__name__)

db_connection = DBConnectionHandler()
db_connection.get_db_engine()

app.register_blueprint(user_routes)
