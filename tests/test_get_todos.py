from utils.api_client import get_todos, get_todo_by_id

def test_get_all_todos_status_code():
    response = get_todos()
    print(f"Status code received: {response.status_code}")
    assert response.status_code == 200

def test_get_all_todos_returns_list():
    response = get_todos()
    data = response.json()
    assert isinstance(data, list)

def test_get_single_todo_status_code():
    response = get_todo_by_id(1)
    assert response.status_code == 200

def test_get_single_todo_has_required_fields():
    response = get_todo_by_id(1)
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "completed" in data
    assert "userId" in data

def test_get_single_todo_field_types():
    response = get_todo_by_id(1)
    data = response.json()
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["completed"], bool)

def test_get_single_todo_correct_id_returned():
    response = get_todo_by_id(5)
    data = response.json()
    assert data["id"] == 5