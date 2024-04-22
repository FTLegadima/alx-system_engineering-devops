import requests
import sys

def fetch_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code != 200 or todos_response.status_code != 200:
            print("Error: Could not fetch data from API.")
            return

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data['name']
        total_tasks = len(todos_data)
        completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]

        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        print("Error: ", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)
