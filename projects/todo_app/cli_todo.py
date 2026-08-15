import argparse
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError: #if no "tasks.json" yet, create an empty array
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Creates the parser
# Responsible for reading and understanding what the user typed
# decription appears when the user ask for help
parser = argparse.ArgumentParser(description="A simple CLI Todo App")

# Add subcommands
# `dest="command"` -> Whatever the user type -> stores in command variable
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Subcommand: add
add_parser = subparsers.add_parser("add", help="Add a new task")
# Tell the subparser what to add
# When someone uses the add command, they must provide a task
add_parser.add_argument("task", type=str, help="The task description")

# Subcommand: list
list_parser = subparsers.add_parser("list", help="List all tasks")

#Subcommand: delete
delete_parser = subparsers.add_parser("delete", help="Delete a task by number")
delete_parser.add_argument("index", type=int, help="The number of the task to delete")

# 3. Parse the arguments that the user typed in the terminal
args = parser.parse_args()

# 4. Route to the right logic
if args.command == "add":
    print(f"Adding task: {args.task}")
    tasks = load_tasks()
    tasks.append(args.task)
    save_tasks(tasks)
elif args.command == "list":
    print("Listing all tasks...")
    tasks = load_tasks()
    if tasks == []:
        print("No tasks found!")
    else:
        for index, task in enumerate(tasks):
            print(f"{[index + 1]}{task}")
elif args.command == "delete":
    tasks = load_tasks()
    if tasks == []:
        print("No tasks found!")
    else:
        for index, task in enumerate(tasks):
            print(f"{[index + 1]}{task}")
    print(f"Deleting task: {args.index}")
    target_index = int(args.index) - 1
    tasks.pop(target_index)
    save_tasks(tasks)
    print("Task deleted!")
else:
    parser.print_help()