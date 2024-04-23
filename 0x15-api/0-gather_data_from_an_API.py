import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    
    # Fetch user data
    user_response = requests.get(f'{url}users/{user_id}').json()
    if 'name' not in user_response:
        print("User not found.")
        sys.exit(1)
    employee_name = user_response["name"]

    # Fetch todos for the user
    todos_response = requests.get(f'{url}todos?userId={user_id}').json()
    completed_tasks_response = [task for task in todos_response if task["completed"]]
    total_tasks = len(todos_response)
    completed_tasks = len(completed_tasks_response)

    # Print employee name and task completion status
    print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')

    # Print each completed task
    for task in completed_tasks_response:
        print(f'\t{task["title"]}')

if __name__ == "__main__":
    main()

