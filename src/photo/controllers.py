from werkzeug.datastructures import FileStorage
from src.photo.models import Photo
from src.photo.repo import RepoReadPhoto, RepoWritePhoto


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
