from flask import jsonify, Blueprint, request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
)
from src.photo.controllers import (
    add_like_on_photo,
    get_all_photos,
    get_photos_approved_or_not,
    get_photo_from_request,
    make_photo_approved,
    make_upload_photo,
)
from src.user.controllers import user_is_bride_or_groom


photo_routes = Blueprint("photo_routes", __name__)


@photo_routes.route("/api/photo", methods=["POST"])
@jwt_required()
def post_photo():

    photo_params = get_photo_from_request(request)

    try:
        photo = make_upload_photo(photo_params)

        if photo:
            return jsonify({"data": photo.link_aws}), 201

        return (
            jsonify(
                {
                    "status_code": 400,
                    "body": {"error": "Didn't possible make this upload"},
                }
            ),
            400,
        )

    except Exception as error:
        return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400


@photo_routes.route("/api/photo", methods=["GET"])
@jwt_required()
def get_photo():

    params = request.args.to_dict()
    try:
        if "approved" in params:
            photos = get_photos_approved_or_not(params["approved"])
        else:
            photos = get_all_photos()

        if photos:
            return (
                jsonify(
                    {
                        "data": [
                            {
                                "id": str(photo.id),
                                "url": str(photo.link_aws),
                            }
                            for photo in photos
                        ]
                    }
                ),
                200,
            )

        return jsonify({"data": "Nobody photo"}), 200

    except Exception as error:
        return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400


@photo_routes.route("/api/photo", methods=["PATCH"])
@jwt_required()
def patch_photo():

    params = request.args.to_dict()
    body = request.json
    user_id = get_jwt_identity()

    try:
        if user_is_bride_or_groom(user_id):
            if "id" in params and "approved" in body.keys():

                photo = make_photo_approved(id=params["id"], approved=body["approved"])

                return (
                    jsonify(
                        {
                            "data": {
                                "id": str(photo.id),
                                "url": str(photo.link_aws),
                            }
                        }
                    ),
                    200,
                )

            return jsonify({"data": "Nobody photo"}), 200

        return jsonify({"data": "Only groom or bride can make this"}), 401

    except Exception as error:
        return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400


@photo_routes.route("/api/photo/<photo_id>/liked", methods=["POST"])
@jwt_required()
def liked_a_photo(photo_id):

    body = request.json
    user_id = get_jwt_identity()

    try:
        if user_is_bride_or_groom(user_id):
            if photo_id and "id" in body:

                photo_liked = add_like_on_photo(photo_id=photo_id, user_id=body["id"])

                if photo_liked:
                    return (
                        jsonify(
                            {
                                "data": {
                                    "id": str(photo_liked.id),
                                    "who_liked": photo_liked.who_liked,
                                }
                            }
                        ),
                        200,
                    )

                return (
                    jsonify({"data": "Already liked for you!"}),
                    200,
                )

            return jsonify({"data": "Nobody photo"}), 200

        return jsonify({"data": "Only groom or bride can make this"}), 401

    except Exception as error:
        return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400
