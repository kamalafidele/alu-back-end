#!/usr/bin/python3
"""
Fetches and displays the TODO list progress of a given employee.
"""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1] if len(sys.argv) > 1 else None
    if user_id is None or not user_id.isdigit():
        sys.exit(1)

    user_id = int(user_id)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed") is True]
    done_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_count, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

