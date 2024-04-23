#!/usr/bin/python3
"""Retrieve and display employee's TODO list progress"""

import requests
import sys

def main():
    """Main function to retrieve and display employee's TODO list progress"""
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Define base URL
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user data
    user_response = requests.get(f'{base_url}users/{employee_id}')
    user_data = user_response.json()
    if 'name' not in user_data:
        print("User not found.")
        sys.exit(1)
    employee_name = user_data["name"]

    # Fetch user's todos
    todos_response = requests.get(f'{base_url}todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Fetch completed todos
    completed_response = requests.get(f'{base_url}todos?userId={employee_id}&completed=true')
    completed_todos = completed_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = len(completed_todos)

    # Print progress
    print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
    for task in completed_todos:
        print(f'\t{task["title"]}')

if __name__ == "__main__":
    main()
