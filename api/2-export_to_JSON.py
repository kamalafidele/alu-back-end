#!/usr/bin/python3
"""
Exports an employee's TODO list to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1] if len(sys.argv) > 1 else None
    if user_id is None or not user_id.isdigit():
        sys.exit(1)

    user_id = int(user_id)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")
    filename = "{}.json".format(user_id)

    task_list = []
    for task in todos_data:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_data = {str(user_id): task_list}

    with open(filename, mode="w") as file:
        json.dump(json_data, file)

