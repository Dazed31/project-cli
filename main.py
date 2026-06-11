import argparse
from models.user import User
from utils.storage import load_data, save_data

def add_user(args):
    data = load_data()

    user = {
        "name": args.name,
        "email": args.email,
        "projects": []
    }

    data["users"].append(user)
    save_data(data)

    print(f"User {args.name} added.")
import argparse
from models.user import User
from utils.storage import load_data, save_data

def add_user(args):
    data = load_data()

    user = {
        "name": args.name,
        "email": args.email,
        "projects": []
    }

    data["users"].append(user)
    save_data(data)

    print(f"User {args.name} added.")

def list_users(args):
    data = load_data()

    for user in data["users"]:
        print(f"{user['name']} - {user['email']}")

def main():
    parser = argparse.ArgumentParser(description="Project CLI Tool")
    subparsers = parser.add_subparsers()

    # add-user
    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    # list-users
    list_parser = subparsers.add_parser("list-users")
    list_parser.set_defaults(func=list_users)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
def list_users(args):
    data = load_data()

    for user in data["users"]:
        print(f"{user['name']} - {user['email']}")

def main():
    parser = argparse.ArgumentParser(description="Project CLI Tool")
    subparsers = parser.add_subparsers()

    # add-user
    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    # list-users
    list_parser = subparsers.add_parser("list-users")
    list_parser.set_defaults(func=list_users)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()