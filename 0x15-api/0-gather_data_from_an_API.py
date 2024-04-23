#!/usr/bin/python3
"""Retrieve and display employee's TODO list progress"""

import sys
import requests

def fetch_todo_progress(employee_id):
    """Fetch and display employee's TODO list progress"""
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user data
    user_response = requests.get(f'{base_url}users/{employee_id}')
    user_data = user_response.json()
    if 'name' not in user_data:
        print("User not found.")
        return

    employee_name = user_data["name"]

    # Fetch user's todos
    todos_response = requests.get(f'{base_url}todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task["completed"])

    # Print progress
    print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
    for task in todos_data:
        if task["completed"]:
            print(f'\t{task["title"]}')

if __name__ == "__main__":
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_progress(employee_id)

