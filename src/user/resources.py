from flask import jsonify, Blueprint, request
from src.user.repo import RepoReadUser, RepoWriteUser


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/api/users", methods=["GET"])
def get_user():

    user_params = request.json if hasattr(request, "json") else {}

    if "users" in user_params.keys():
        try:
            users = RepoReadUser().get_users_by_id(user_params["users"])

        except Exception as error:
            return jsonify({"status_code": 400, "body": {"error": error}}), 400

        message = [
            {
                "id": str(user.id),
                "attributes": {
                    "email": str(user.email),
                    "name": str(user.name),
                    "is_bride_or_groom": bool(user.is_bride_or_groom),
                },
            }
            for user in users
        ]

        return jsonify({"data": message}), 200

    try:
        users = RepoReadUser().get_all_users()
        message = [
            {
                "id": str(user.id),
                "attributes": {
                    "email": str(user.email),
                    "name": str(user.name),
                    "is_bride_or_groom": bool(user.is_bride_or_groom),
                },
            }
            for user in users
        ]
        return jsonify({"data": message}), 200

    except Exception as error:
        return jsonify({"status_code": 400, "body": {"error": error}}), 400


@user_routes.route("/api/users", methods=["POST"])
def post_user():

    user_params = request.json

    if set(["email", "is_bride_or_groom", "name", "password"]).intersection(
        user_params.keys()
    ):

        try:
            user = RepoWriteUser().create_user(
                email=user_params["email"],
                is_bride_or_groom=user_params["is_bride_or_groom"],
                name=user_params["name"],
                password=user_params["password"],
            )
        except Exception as error:
            return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400

        message = {
            "type": "Users",
            "id": str(user.id),
            "attributes": {"name": str(user.name)},
        }

        return jsonify({"data": message}), 201

    return jsonify({"status_code": 400, "body": {"error": "Incomplete Datas"}}), 400
