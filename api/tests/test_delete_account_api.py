def test_delete_account():

    response = api.delete_account(
        "apiuser123@gmail.com",
        "Test123"
    )

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["responseCode"] == 200