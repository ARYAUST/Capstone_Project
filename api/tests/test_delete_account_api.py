def test_delete_account(api):

    api.create_account({
        "name": "Delete Test User",
        "email": "apiuser123@gmail.com",
        "password": "Test123",
        "title": "Mr",
        "firstname": "Delete",
        "lastname": "User",
        "country": "India"
    })

    response = api.delete_account(
        "apiuser123@gmail.com",
        "Test123"
    )

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["responseCode"] == 200