from flask import jsonify, Blueprint, request
from src.photo.repo import RepoReadPhoto, RepoWritePhoto


photo_routes = Blueprint("photo_routes", __name__)


@photo_routes.route("/api/photo", methods=["POST"])
def post_photo():

    photo_params = request.files

    try:
        photo = RepoWritePhoto().upload_photo(list(photo_params.values())[0])
    except Exception as error:
        return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400

    return jsonify({"data": photo.link_aws}), 201


@photo_routes.route("/api/photo", methods=["GET"])
def get_photo():

    params = request.args.to_dict()

    if "approved" in params:
        try:
            if params["approved"] == "true":
                photos = RepoReadPhoto().get_all_approved_photos()
            else:
                photos = RepoReadPhoto().get_all_not_approved_photos()

            if photos:
                print(photos)
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

    try:
        photos = RepoReadPhoto().get_all_photos()

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
def patch_photo():

    params = request.args.to_dict()
    body = request.json

    if "id" in params:
        try:
            photo = RepoReadPhoto().get_one_photo_by_id(params["id"])

            if photo and "approved" in body.keys():
                photo.approved = True if body["approved"] else False
                photo.save()

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

        except Exception as error:
            return jsonify({"status_code": 400, "body": {"error": str(error)}}), 400
