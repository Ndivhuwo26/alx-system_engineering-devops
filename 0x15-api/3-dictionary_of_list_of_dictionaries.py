
#!/usr/bin/python3
"""this a python script to fetch Rest API for todo lists of employees"""
import json
import requests

def fetch_employee_tasks():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    
    users = users_response.json()
    todos = todos_response.json()
    
    user_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        
        user_tasks[user_id] = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user_id
        ]
    
    return user_tasks

def export_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    all_tasks = fetch_employee_tasks()
    export_to_json(all_tasks, "todo_all_employees.json")

