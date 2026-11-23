def test_update_account(api):

    user = {
        "name": "Updated User",
        "email": "apiuser123@gmail.com",
        "password": "Test123",
        "firstname": "Updated",
        "lastname": "User",
        "company": "UST Global",
        "address1": "Kochi",
        "country": "India"
    }

    response = api.update_account(user)

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["responseCode"] == 200