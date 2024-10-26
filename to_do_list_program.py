import sys
task = []

print("================================================")
print(f"{"To - Do - List":^50}")
print("================================================")

while True:
    print("1. Add an item")
    print("2. Mark Task as completed")
    print("3. Remove a Task")
    print("4. View the Task")
    print("5. Exit")
    print("================================================")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        task.append(item)
        print(f"{item} added to the list.")
        print("================================================")

    elif choice == '2':
        item = input("Enter the item to mark as completed: ")
        if item in task:
            task.remove(item)
            print(f"{item} marked as completed.")
        else:
            print(f"{item} is not in the list.")
        print("================================================")
    elif choice == '3':
        item = input("Enter the item to remove: ")
        if item in task:
            task.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} is not in the list.")
        print("================================================")
    elif choice == '4':
        print("================================================")
        print(f"{'Task List':^50}")
        print("================================================")
        if not task:
            print("No tasks in the list.")
        else:
            for i, item in enumerate(task):
                print(f"{i+1}. {item}")
        print("================================================")
    elif choice == '5':
        print("Exiting the program...")
        sys.exit()
else:
    print("Invalid choice. Please try again.")

    