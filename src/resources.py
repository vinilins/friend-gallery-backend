from src.auth.resources import login_routes
from src.photo.resources import photo_routes
from src.user.resources import user_routes


def resources_init_app(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(login_routes)
    app.register_blueprint(photo_routes)
