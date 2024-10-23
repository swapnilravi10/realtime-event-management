from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_event():
    response = client.post("/api/create-event/", json={
        "title": "Sample Event",
        "organizer": "Alice",
        "date_time": "2024-10-23 10:00",
        "duration": 2,
        "location": "New York"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Event created"

def test_join_event():
    response = client.post("/api/create-event/", json={
        "title": "Sample Event",
        "organizer": "Alice",
        "date_time": "2024-10-23 10:00",
        "duration": 2,
        "location": "New York"
    })
    event_id = response.json()["event_id"]
    join_response = client.post(f"/join_event/{event_id}", json={"username": "Bob"})
    assert join_response.status_code == 200
    assert join_response.json()["message"] == "Bob joined the event"
