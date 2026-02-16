import requests

# Base URL for the microservice
BASE_URL = "http://localhost:5001"


def test_export_json():
    """Test exporting data to JSON format."""
    
    print("=" * 50)
    print("TEST 1: Export to JSON")
    print("=" * 50)
    
    url = f"{BASE_URL}/export"
    payload = {
        "data": {
            "tasks": [
                {"id": 1, "text": "Buy groceries", "completed": False},
                {"id": 2, "text": "Finish CS361 assignment", "completed": True}
            ]
        },
        "format": "json"
    }
    
    print(f"Request URL: {url}")
    print(f"Request Body: {payload}")
    print()
    
    response = requests.post(url, json=payload)
    
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.json()}")
    print()


def test_export_text():
    """Test exporting data to plain text format."""
    
    print("=" * 50)
    print("TEST 2: Export to Text")
    print("=" * 50)
    
    url = f"{BASE_URL}/export"
    payload = {
        "data": {
            "tasks": [
                {"id": 1, "text": "Buy groceries", "completed": False},
                {"id": 2, "text": "Finish CS361 assignment", "completed": True}
            ]
        },
        "format": "text"
    }
    
    print(f"Request URL: {url}")
    print(f"Request Body: {payload}")
    print()
    
    response = requests.post(url, json=payload)
    
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.json()}")
    print()


def test_invalid_request():
    """Test error handling for invalid requests."""
    
    print("=" * 50)
    print("TEST 3: Error Handling (Missing Data)")
    print("=" * 50)
    
    url = f"{BASE_URL}/export"
    payload = {
        "format": "json"
        # Missing 'data' field
    }
    
    print(f"Request URL: {url}")
    print(f"Request Body: {payload}")
    print()
    
    response = requests.post(url, json=payload)
    
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.json()}")
    print()


if __name__ == '__main__':
    print("\n*** DATA EXPORT MICROSERVICE - TEST PROGRAM ***\n")
    
    test_export_json()
    test_export_text()
    test_invalid_request()
    
    print("=" * 50)
    print("ALL TESTS COMPLETED")
    print("=" * 50)
