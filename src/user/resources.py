from flask import jsonify, Blueprint, request
from src.user.controllers import (
    create_new_user,
    get_users_by_id,
    get_all_users_registered,
)


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/api/users", methods=["GET"])
def get_user():

    user_params = request.json if hasattr(request, "json") else {}

    try:
        if "users" in user_params.keys():

            message = get_users_by_id(user_params["users"])
            return jsonify({"data": message}), 200

        message = get_all_users_registered()
        return jsonify({"data": message}), 200

    except Exception as error:
        return jsonify({"status_code": 400, "body": {"error": error}}), 400


@user_routes.route("/api/users", methods=["POST"])
def post_user():

    user_params = request.json

    if "email" and "is_bride_or_groom" and "name" and "password" in user_params.keys():
        try:
            message = create_new_user(user_params)
            return jsonify({"data": message}), 201

        except Exception as error:
            return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400

    return jsonify({"status_code": 400, "body": {"error": "Incomplete Datas"}}), 400
