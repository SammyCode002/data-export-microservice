# Data Export Microservice

## Description

This microservice converts data into JSON or plain text format for export/download. It accepts any data structure and returns it formatted according to the requested output format.

**Developers:** Devin Gaughan, Samuel Dameg

---

## Communication Contract

### How to REQUEST Data

**Endpoint:** `POST /export`

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| data | object | Yes | The data to export (any valid JSON object) |
| format | string | Yes | Output format: "json" or "text" |

**Example Request (Python):**

```python
import requests

url = "http://localhost:5001/export"
payload = {
    "data": {
        "tasks": [
            {"id": 1, "text": "Buy groceries", "completed": False},
            {"id": 2, "text": "Finish assignment", "completed": True}
        ]
    },
    "format": "json"
}

response = requests.post(url, json=payload)
```

---

### How to RECEIVE Data

**Response Format:** JSON

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| success | boolean | True if export was successful |
| format | string | The format used ("json" or "text") |
| exported_data | object/string | The exported data in requested format |
| error | string | Error type (only if success is false) |
| message | string | Error message (only if success is false) |

**Example Response (JSON format):**

```json
{
    "success": true,
    "format": "json",
    "exported_data": {
        "tasks": [
            {"id": 1, "text": "Buy groceries", "completed": false},
            {"id": 2, "text": "Finish assignment", "completed": true}
        ]
    }
}
```

**Example Response (Text format):**

```json
{
    "success": true,
    "format": "text",
    "exported_data": "TASKS:\n  Item 1:\n    id: 1\n    text: Buy groceries\n    completed: False\n  Item 2:\n    id: 2\n    text: Finish assignment\n    completed: True"
}
```

**Error Response Example:**

```json
{
    "success": false,
    "error": "Missing field",
    "message": "Request must include 'data' field"
}
```

---

## UML Sequence Diagram

```
┌─────────────────┐                      ┌─────────────────────┐
│  Test Program   │                      │ Data Export Service │
│  (Client)       │                      │   (localhost:5001)  │
└────────┬────────┘                      └──────────┬──────────┘
         │                                          │
         │  POST /export                            │
         │  {data: {...}, format: "json"}           │
         │─────────────────────────────────────────>│
         │                                          │
         │                                          │ validate request
         │                                          │ format data
         │                                          │
         │  200 OK                                  │
         │  {success: true, exported_data: {...}}  │
         │<─────────────────────────────────────────│
         │                                          │
         │                                          │
         │  POST /export                            │
         │  {format: "json"}  (missing data)        │
         │─────────────────────────────────────────>│
         │                                          │
         │  400 Bad Request                         │
         │  {success: false, error: "..."}         │
         │<─────────────────────────────────────────│
         │                                          │
```

---

## Running the Microservice

1. Install dependencies:
   ```
   pip install flask requests
   ```

2. Start the microservice:
   ```
   python app.py
   Or:
   py app.py
   ```

3. Run the test program (in a new terminal):
   ```
   python test_program.py
   Or:
   py test_program.py
   ```

---

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request (missing/invalid parameters) |
