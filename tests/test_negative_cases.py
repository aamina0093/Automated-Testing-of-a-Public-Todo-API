from utils.api_client import get_todo_by_id

def test_get_nonexistent_todo_returns_404():
    response = get_todo_by_id(99999)
    assert response.status_code == 404

def test_get_todo_with_invalid_id_string():
    response = get_todo_by_id("abc")
    assert response.status_code == 404