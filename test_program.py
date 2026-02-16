import requests

# Base URL for the microservice
BASE_URL = "http://localhost:5001"


def test_export_tasks_json():
    """Test exporting tasks to JSON format (Samuel's To-Do List)."""
    
    print("=" * 50)
    print("TEST 1: Export Tasks to JSON (Samuel's To-Do List)")
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


def test_export_characters_json():
    """Test exporting characters to JSON format (Devin's Character Lore Tracker)."""
    
    print("=" * 50)
    print("TEST 2: Export Characters to JSON (Devin's Lore Tracker)")
    print("=" * 50)
    
    url = f"{BASE_URL}/export"
    payload = {
        "data": {
            "characters": [
                {
                    "id": 1,
                    "name": "Kira Voss",
                    "race": "Human",
                    "class": "Space Pilot",
                    "items": ["Plasma Blaster", "Navigation Chip"]
                },
                {
                    "id": 2,
                    "name": "Zor'ak the Wise",
                    "race": "Elf",
                    "class": "Mage",
                    "items": ["Staff of Fire", "Ancient Spellbook"]
                }
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


def test_export_characters_text():
    """Test exporting characters to text format (Devin's Character Lore Tracker)."""
    
    print("=" * 50)
    print("TEST 3: Export Characters to Text (Devin's Lore Tracker)")
    print("=" * 50)
    
    url = f"{BASE_URL}/export"
    payload = {
        "data": {
            "characters": [
                {
                    "id": 1,
                    "name": "Kira Voss",
                    "race": "Human",
                    "class": "Space Pilot",
                    "items": ["Plasma Blaster", "Navigation Chip"]
                }
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
    print("TEST 4: Error Handling (Missing Data)")
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
    
    test_export_tasks_json()
    test_export_characters_json()
    test_export_characters_text()
    test_invalid_request()
    
    print("=" * 50)
    print("ALL TESTS COMPLETED")
    print("=" * 50)
