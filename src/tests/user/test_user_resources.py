class TestUserResources:
    def test_create_user(self, client, mocker):
        mocker.patch("src.user.controllers.create_new_user", return_value=object())
        data = {
            "email": "vinicius@gmail.com",
            "name": "Vinicius Lins",
            "password": "abcd123",
            "is_bride_or_groom": True,
        }

        response = client.post("/api/users", json=data)
        assert response.status_code == 201
        assert "Vinicius Lins" in response.data.decode()

    def test_get_user(self, client, mocker):
        mocker.patch(
            "src.user.controllers.get_all_users_registered", return_value=object()
        )
        data = {
            "email": "vinicius@gmail.com",
            "name": "Vinicius Lins",
            "password": "abcd123",
            "is_bride_or_groom": True,
        }

        response = client.post("/api/users", json=data)
        assert response.status_code == 201
        assert "Vinicius Lins" in response.data.decode()

        # GET
        response = client.get("/api/users", json=data)
        assert response.status_code == 200
        assert "Vinicius Lins" in response.data.decode()
