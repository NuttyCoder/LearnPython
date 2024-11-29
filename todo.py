# todo.py

import os

# Function to display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")
    print("Tasks saved to file.")

# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Options:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Save tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
