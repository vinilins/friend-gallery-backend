import jwt

from datetime import datetime, timedelta
from flask import jsonify, Blueprint, request
from os import getenv
from src.user.repo import RepoReadUser


login_routes = Blueprint("login_routes", __name__)


@login_routes.route("/api/login", methods=["POST"], strict_slashes=False)
def login():

    login_params = request.get_json()

    if "email" in login_params.keys() and "password" in login_params.keys():
        user = RepoReadUser().get_one_user_by_email(email=login_params["email"])

        if user:
            password = user.password
            email = user.email

            if email == login_params["email"] and password == login_params["password"]:

                access_token = jwt.encode(
                    {"exp": datetime.utcnow() + timedelta(days=1)},
                    key=getenv("AUTHENTICATION_TOKEN_PASSWORD"),
                    algorithm="HS256",
                )

                return jsonify({"accessToken": access_token}), 200

            return (
                jsonify({"status_code": 401, "body": {"error": "Incorrect Datas!"}}),
                401,
            )

        return jsonify({"status_code": 401, "body": {"error": "Incorrect User!"}}), 401

    return jsonify({"status_code": 400, "body": {"error": "Incomplete Datas"}}), 400
