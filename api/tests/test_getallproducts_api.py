from playwright.sync_api import Playwright
def test_get_all_products(playwright: Playwright):
    # Create API request context
    request = playwright.request.new_context(
        base_url="https://automationexercise.com",
        ignore_https_errors=True
    )
    # Send GET request
    response = request.get("/api/productsList")
    # Validate HTTP status
    assert response.status == 200
    # Convert response into JSON
    response_data = response.json()
    # Validate response body
    assert response_data["responseCode"] == 200
    assert "products" in response_data
    print("Products API tested successfully")
    request.dispose()