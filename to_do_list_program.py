import sys
import os
import time

def clear_screen():
    if os.name == 'nt':
        _ = os.system("cls")
    else:
        _ = os.system("clear")

task = []
def add_task():
    print("================================================")
    print(f"{"Add Task":^50}")
    print("================================================")
    tasks = input("Enter task name: ")
    task.append(tasks)
    print(f"{tasks} added to the list.")
    print("================================================")
    print()

def mark_task_complete():
    print("================================================")
    print(f"{"Mark Task As Complete":^50}")
    print("================================================")
    tasks = input("Enter the task to mark as completed: ")
    if tasks in task:
        task.remove(tasks)
        print(f"{tasks} marked as completed.")
    else:
        print(f"{tasks} is not in the list.")
    print("================================================")
    print()

def remove_task():
    print("================================================")
    print(f"{"Remove Task":^50}")
    print("================================================")
    item = input("Enter the item to remove: ")
    if item in task:
        task.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} is not in the list.")
    print("================================================")
    print()

def view_task():
    print("================================================")
    print(f"{'Task List':^50}")
    print("================================================")
    if not task:
        print("No tasks in the list.")
    else:
        for i, item in enumerate(task):
            print(f"{i+1}. {item}")
    print("================================================")
    print()

while True:
    print("================================================")
    print(f"{"To - Do - List":^50}")
    print("================================================")
    print("1. Add Task")
    print("2. Mark Task as completed")
    print("3. Remove a Task")
    print("4. View the Task")
    print("5. Exit")
    print("================================================")
    choice = input("Enter your choice (1-5): ")
    clear_screen()

    if choice == '1':
        add_task()
    elif choice == '2':
        mark_task_complete()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        view_task()
    elif choice == '5':
        print("Exiting the program...")
        sys.exit()
else:
    print("Invalid choice. Please try again.")

    