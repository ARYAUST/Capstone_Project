def test_verify_login(api):

    api.create_account({
        "name": "Login Test User",
        "email": "apiuser123@gmail.com",
        "password": "Test123",
        "title": "Mr",
        "firstname": "Login",
        "lastname": "User",
        "country": "India"
    })

    response = api.verify_login(
        "apiuser123@gmail.com",
        "Test123"
    )

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["responseCode"] == 200