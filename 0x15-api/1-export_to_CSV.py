#!/usr/bin/python3
"""this will Export API data to CSV format"""
import csv
import requests
import sys

def export_to_csv(user_id):
    
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


    csv_filename = f"{user_id}.csv"

    
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
            ])

    print(f"Data for user {user_id} has been written to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_csv(user_id)

