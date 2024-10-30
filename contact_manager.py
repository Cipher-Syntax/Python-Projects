import os
import sys
import time

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
contact_list = {}

def add_contact():
    name = input("Enter name to add: ")
    phone_number = input("Enter phone number to add: ")
   
    print()
    if name in contact_list:
        print(f"Contact '{name}' already exists. Updating contact details.")
    else:
        print(f"Adding new contact '{name}'.")

    contact_list[name] = phone_number
    print(f"Contact '{name}' has been added/updated successfully.")

def display_contacts():
    if len(contact_list) == 0:
        print("No contacts found.")
    else:
        for name, phone_number in contact_list.items():
            print(f"{name}: {phone_number}")
  
def update_contact():
    update_contact = input("Enter the name of the contact you want to update: ")
    if update_contact in contact_list:
        new_phone_number = input("Enter the new phone number: ")
        contact_list[update_contact] = new_phone_number
        print(f"Contact '{update_contact}' has been updated successfully.")
    else:
        print(f"Contact '{update_contact}' not found.")

def delete_contact():
    del_contact = input("Enter the contact you want to delete: ")
    if del_contact in contact_list:
        print(f"Contact '{del_contact}' has been deleted successfully.")
        del contact_list[del_contact]
    else:
        print(f"Contact '{del_contact}' not found.")


def main():
    while True:
        print("======================================================")
        print(f"{'Contact Manager':^50}")
        print("======================================================")
        try:
            print("1. Add Contact")
            print("2. Display Contacts")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Exit")
            print("======================================================")
            user_choice = int(input("Enter your choice (1 - 5): "))
            clear_screen()
            
            if user_choice == 1:
                print("======================================================")
                print(f"{'Add Contact':^50}")
                print("======================================================")
                add_contact()
                print("\nreturning to menu.....")
                time.sleep(1)
            elif user_choice == 2:
                print("======================================================")
                print(f"{'Display Contact':^50}")
                print("======================================================")
                display_contacts()
                print("\nreturning to menu.....")
                time.sleep(1)
            elif user_choice == 3:
                print("======================================================")
                print(f"{'Update Contact':^50}")
                print("======================================================")
                update_contact()
                print("\nreturning to menu.....")
                time.sleep(1)
            elif user_choice == 4:
                print("======================================================")
                print(f"{'Delete Contact':^50}")
                print("======================================================")
                delete_contact()
                print("\nreturning to menu.....")
                time.sleep(1)
                
            elif user_choice == 5:
                print("Exiting...")
                sys.exit()

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()