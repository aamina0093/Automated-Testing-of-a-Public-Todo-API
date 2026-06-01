# ALL API CALLS ARE STORED HERE.

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_todos():
    return requests.get(f"{BASE_URL}/todos")

def get_todo_by_id(todo_id):
    return requests.get(f"{BASE_URL}/todos/{todo_id}")

def create_todo(payload):
    return requests.post(f"{BASE_URL}/todos", json=payload)

def get_todos_by_user(user_id):
    return requests.get(f"{BASE_URL}/todos", params={"userId": user_id})