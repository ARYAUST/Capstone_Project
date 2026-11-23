from api.api_client import AutomationExerciseAPI


def test_search_product():
    api = AutomationExerciseAPI()
    response = api.search_product("top")

    assert response.status_code == 200

    json_data = response.json()
    assert json_data["responseCode"] == 200
    assert len(json_data["products"]) > 0