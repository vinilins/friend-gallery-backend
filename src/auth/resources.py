from flask import jsonify, Blueprint, request
from src.auth.controllers import create_acess_token, corrects_credentials


login_routes = Blueprint("login_routes", __name__)


@login_routes.route("/api/login", methods=["POST"], strict_slashes=False)
def login():

    login_params = request.get_json()

    if "email" in login_params.keys() and "password" in login_params.keys():
        user, correct = corrects_credentials(login_params)

        if correct and user:

            token = create_acess_token(user.id)

            return jsonify({"token": str(token)}), 200
        print(f"\noi: {user}, {correct}\n")
        return (
            jsonify({"status_code": 401, "body": {"error": "Incorrect Datas!"}}),
            401,
        )

    return jsonify({"status_code": 401, "body": {"error": "Incomplete Datas"}}), 401
