def test_verify_login():

    response = api.verify_login(
        "testuser@gmail.com",
        "Test123"
    )

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["responseCode"] == 200