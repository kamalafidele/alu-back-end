#!/usr/bin/python3
"""
Exports TODO list data of all employees to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit(1)

    users_data = users_response.json()
    todos_data = todos_response.json()

    all_tasks = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []

        for task in todos_data:
            if task.get("userId") == user_id:
                tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        all_tasks[str(user_id)] = tasks

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(all_tasks, file)

