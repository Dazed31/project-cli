import argparse
import json
import os

DATA_FILE_PATH = "data/data.json"


# -------------------- DATA HANDLING --------------------
def load_data():
    if not os.path.exists(DATA_FILE_PATH):
        return {"users": []}

    with open(DATA_FILE_PATH, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


# -------------------- USER FUNCTIONS --------------------
def add_user(arguments):
    data = load_data()

    for user in data["users"]:
        if user["name"] == arguments.name:
            print("User already exists")
            return

    new_user = {
        "name": arguments.name,
        "email": arguments.email,
        "projects": []
    }

    data["users"].append(new_user)
    save_data(data)

    print(f"User {arguments.name} added.")


def list_users(arguments):
    data = load_data()

    for user in data["users"]:
        print(f"{user['name']} - {user['email']}")


# -------------------- PROJECT FUNCTIONS --------------------
def add_project(arguments):
    data = load_data()

    for user in data["users"]:
        if user["name"] == arguments.user_name:
            new_project = {
                "title": arguments.title,
                "description": arguments.description,
                "tasks": []
            }

            user["projects"].append(new_project)
            save_data(data)

            print(f"Project {arguments.title} added to {arguments.user_name}")
            return

    print("User not found")


def list_projects(arguments):
    data = load_data()

    for user in data["users"]:
        if user["name"] == arguments.user_name:
            for project in user["projects"]:
                print(f"{project['title']} - {project['description']}")
            return

    print("User not found")


# -------------------- TASK FUNCTIONS --------------------
def add_task(arguments):
    data = load_data()

    for user in data["users"]:
        for project in user["projects"]:
            if project["title"] == arguments.project_title:
                new_task = {
                    "title": arguments.title,
                    "status": "pending"
                }

                project["tasks"].append(new_task)
                save_data(data)

                print(f"Task {arguments.title} added to {arguments.project_title}")
                return

    print("Project not found")


def complete_task(arguments):
    data = load_data()

    for user in data["users"]:
        for project in user["projects"]:
            if project["title"] == arguments.project_title:
                for task in project["tasks"]:
                    if task["title"] == arguments.title:
                        task["status"] = "completed"
                        save_data(data)

                        print(f"Task {arguments.title} marked as completed")
                        return

    print("Task not found")


# -------------------- CLI SETUP --------------------
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # add user
    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    # list users
    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)

    # add project
    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("--user-name", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", default="")
    add_project_parser.set_defaults(func=add_project)

    # list projects
    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.add_argument("--user-name", required=True)
    list_projects_parser.set_defaults(func=list_projects)

    # add task
    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("--project-title", required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.set_defaults(func=add_task)

    # complete task
    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("--project-title", required=True)
    complete_task_parser.add_argument("--title", required=True)
    complete_task_parser.set_defaults(func=complete_task)

    arguments = parser.parse_args()

    if hasattr(arguments, "func"):
        arguments.func(arguments)


if __name__ == "__main__":
    main()