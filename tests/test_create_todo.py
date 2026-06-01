from utils.api_client import create_todo

def test_create_todo_status_code():
    payload = {"title": "Buy groceries", "completed": False, "userId": 1}
    response = create_todo(payload)
    assert response.status_code == 201      # api code for creation

def test_create_todo_response_contains_id():
    payload = {"title": "Study Pytest", "completed": False, "userId": 2}
    response = create_todo(payload)
    data = response.json()
    assert "id" in data

def test_create_todo_title_matches_input():     # title check
    payload = {"title": "Write test cases", "completed": False, "userId": 3}
    response = create_todo(payload)
    data = response.json()
    assert data["title"] == "Write test cases"
