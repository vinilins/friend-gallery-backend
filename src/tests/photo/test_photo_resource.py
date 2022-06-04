from src.photo.models import Photo


def mock_jwt_required(*args):
    return


class TestPhotoResources:
    def test_upload_photo(self, client, mocker):
        mocker.patch(
            "src.photo.resources.make_upload_photo",
            return_value=Photo(
                link_aws="https://gallery-friend.s3.sa-east-1.amazonaws.com/vini.png"
            ),
        )
        mocker.patch(
            "flask_jwt_extended.view_decorators.verify_jwt_in_request",
            side_effect=mock_jwt_required,
        )

        mocker.patch(
            "src.photo.resources.get_photo_from_request", return_value=object()
        )
        headers = {
            "Content-Type": "form-data",
            "Authorization": "Bearer token",
        }

        response = client.post(
            "/api/photo", data={"key": "vini.png", "value": "hi"}, headers=headers
        )

        assert response.status_code == 201
        assert "vini.png" in response.data.decode()
