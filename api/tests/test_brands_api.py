def test_get_all_brands(api):

    response = api.get_all_brands()

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["responseCode"] == 200
    assert len(json_data["brands"]) > 0