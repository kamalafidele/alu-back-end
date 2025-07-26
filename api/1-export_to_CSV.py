#!/usr/bin/python3
"""
Exports an employee's TODO list to a CSV file.
"""

import csv
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
    filename = "{}.csv".format(user_id)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

