import json

def load_tasks():
    with open("todos.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("todos.json", "w") as file:
        json.dump(tasks, file, indent=4)

while True:
    user_input = input("What do you want to do? [1] View Tasks, [2] Add Task, [3] Delete, [4] Exit\n" \
    "Please enter 1, 2, 3, or 4: ")
    if(user_input == "1"):
        tasks = load_tasks()
        for index, task in enumerate(tasks):
            print(f"[{index + 1}]{task}\n")
    elif(user_input == "2"):
        tasks = load_tasks()
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added!")
    elif(user_input == "3"):
        tasks = load_tasks()
        for index, task in enumerate(tasks):
            print(f"[{index + 1}]{task}\n")
        task_num_str = input("Enter the number of the task to delete: ")
        task_num_int = int(task_num_str) - 1
        tasks.pop(task_num_int)
        save_tasks(tasks)
        print("Task deleted")
    elif(user_input == "4"):
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please type 1, 2, 3, or 4.")

