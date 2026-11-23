def test_create_account(api):

    user = {
        "name": "API User",
        "email": "apiuser123@gmail.com",
        "password": "Test123",
        "title": "Mrs",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1998",
        "firstname": "API",
        "lastname": "User",
        "company": "UST",
        "address1": "Trivandrum",
        "address2": "Kerala",
        "country": "India",
        "zipcode": "695001",
        "state": "Kerala",
        "city": "Trivandrum",
        "mobile_number": "9999999999"
    }

    response = api.create_account(user)

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["responseCode"] == 201