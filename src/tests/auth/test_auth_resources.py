from src.user.models import User


class TestAuthResources:
    def test_login_user(self, client, mocker):
        mocker.patch(
            "src.auth.resources.corrects_credentials",
            return_value=(
                User(
                    email="vinicius@gmail.com",
                    name="vini",
                    password="abcd123",
                    is_bride_or_groom=True,
                ),
                True,
            ),
        )
        mocker.patch(
            "src.auth.resources.create_acess_token",
            return_value="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        )
        data = {"email": "vinicius@gmail.com", "password": "abcd123"}

        response = client.post("/api/login", json=data)

        assert response.status_code == 200
        assert "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" in response.data.decode()
