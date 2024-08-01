#!/usr/bin/python3
"""this will export API data to JSON format"""
import json
import requests
import sys


def export_to_json(user_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"User with id {user_id} not found.")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get('username')

    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    json_data = {str(user_id): tasks}
    json_filename = f"{user_id}.json"

    with open(json_filename, mode='w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"Data for user {user_id} has been written to {json_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_json(user_id)

