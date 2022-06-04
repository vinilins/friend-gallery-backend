import boto3
from werkzeug.datastructures import FileStorage
from src.photo.models import Photo
from src.photo.repo import RepoReadPhoto, RepoWritePhoto


def add_like_on_photo(photo_id, user_id):
    photo = RepoReadPhoto().get_one_photo_by_id(photo_id)

    if photo:
        if user_id not in photo.who_liked:
            RepoWritePhoto().add_like(photo=photo, user_id=user_id)
            return photo

    return None


def get_photo_from_request(request) -> Photo:
    return list(request.files.values())[0]


def make_upload_photo(photo: FileStorage) -> Photo:
    return RepoWritePhoto().upload_photo(photo)


def get_photos_approved_or_not(approved: str) -> list[Photo]:
    if approved == "true":
        return RepoReadPhoto().get_all_approved_photos()

    return RepoReadPhoto().get_all_not_approved_photos()


def get_all_photos() -> list[Photo]:
    return RepoReadPhoto().get_all_photos()


def make_photo_approved(id: str, approved: str) -> Photo:

    photo = RepoReadPhoto().get_one_photo_by_id(id)

    photo.approved = True if approved else False
    photo.save()

    return photo


def s3_init_app(app):
    app.extensions["s3"] = boto3.client(
        "s3",
        aws_access_key_id=app.config["AWS_ID_KEY"],
        aws_secret_access_key=app.config["AWS_PASSWORD_KEY"],
    )
