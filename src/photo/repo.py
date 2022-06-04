from flask import current_app
from src.photo.models import Photo


class RepoReadPhoto:
    """Read Repo Class of the PhotoModel"""

    @staticmethod
    def get_one_photo_by_id(id) -> Photo:
        return Photo.objects(id=id).limit(1).first()

    @staticmethod
    def get_photos_by_id(photos):
        return Photo.objects(id__in=photos)

    @staticmethod
    def get_all_photos():
        return Photo.objects()

    @staticmethod
    def get_all_approved_photos():
        return Photo.objects(approved=True)

    @staticmethod
    def get_all_not_approved_photos():
        return Photo.objects(approved=False)


class RepoWritePhoto:
    """Write Repo Class of the PhotoModel"""

    @staticmethod
    def upload_photo(image) -> Photo:
        s3 = current_app.extensions["s3"]
        bucket_name = current_app.config["AWS_BUCKET"]

        s3.upload_fileobj(Bucket=bucket_name, Fileobj=image, Key=image.name)

        bucket_link_photo = (
            "https://gallery-friend.s3.sa-east-1.amazonaws.com/" + image.name
        )

        try:
            photo = Photo(link_aws=bucket_link_photo)
            photo.save()

            return photo
        except Exception as error:
            raise Exception(f"Error in upload new Photo: {error}")

    @staticmethod
    def add_like(photo, user_id) -> Photo:
        photo.who_liked.append(user_id)
        photo.save()
        return photo
