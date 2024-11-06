import sys
import time
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    

inventory = {}

def add_items():
    try:
        id = int(input("Enter ID #: "))
        product_name = input("Enter product name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        print()
        if id in inventory:
            print("Item already exist....item updated")
        else:
            print(f"{product_name} with id number {id} successfully added to inventory")
            inventory[id] = {"product_name": product_name, "quantity" : quantity, "price" : price }
        print("returning to main menu....")
        time.sleep(1)
        clear_screen()
    except ValueError:
        print("enter a valid id number")

def view_items():
    print("-----INVENTORY-----")
    if len(inventory) == 0:
        print("Inventory is empty...add an item first")
        add_items()
    print(f"{'ID'} {'Product Name':^25} {'Quantity':^25} {'Price':^25}")
    print("----------------------------------------------------------------------")
    for id, item in inventory.items():
        print(f"{'id'} {item['product_name']:^25} {item['quantity']:^25} {item['price']:^25}")

    
def update_items():
    try:
        id = int(input("Enter ID # you want to update: "))
        
        if id in inventory:
            product_name = input("Product Name: ")
            quantity = input("Quantity: ")
            price = input("Price: ")
            
            inventory[id] = {"product_name": product_name, "quantity" : quantity, "price" : price }
            print(f"product with ID number {id} updated successfully")
        else:
            print(f"product with ID number {id} doesn't exist in the inventory")
    except ValueError:
        print("enter a valid id number")
    print("returning to main menu....")
    time.sleep(1)
    clear_screen()   
       
def delete_items():
        id = int(input("Enter ID # to delete: "))
          
        if id in inventory:
            del inventory[id]
            print(f"product with ID number {id} successfully deleted")
        else:
            print(f"product with id number {id} doesn't exist")

        print("returning to main menu....")
        time.sleep(1)
        clear_screen()
              
def search_items():
        id = int(input("Enter ID number you want to check: "))
        if id in inventory:
            print(f"{'ID'} {'Product Name':^25} {'Quantity':^25} {'Price':^25}")
            print("----------------------------------------------------------------------")
            item = inventory[id]
            print(f"{id} {item['product_name']:^25} {item['quantity']:^25} {item['price']:^25}")
        print("returning to main menu....")
        time.sleep(1)
        clear_screen()

def calculate_total_purchases():
    total_purchases = 0
    if len(inventory) == 0:
        print("Inventory is empty...add an item first")
        add_items()

    print(f"{'ID'} {'Product Name':^25} {'Quantity':^25} {'Price':^25}")
    print("----------------------------------------------------------------------")
    for id, item in inventory.items():
        print(f"{'id'} {item['product_name']:^25} {item['quantity']:^25} {item['price']:^25}")
        total_purchases += float(item['quantity']) * float(item['price'])
        
    print()
    print(f"Total Purchases: ${total_purchases}")


def main():

    while True:
        print("-----Inventory Management-----")
        print("1. Add Item")
        print("2. View Item ")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Calculate Total Purchases")
        print("7. Exit")
        print("--------------------------------")
        user_choice = int(input("Enter Choice: "))
        clear_screen()

            
        if user_choice == 1:
            add_items()
            print()
        elif user_choice == 2:
            view_items()
            print()
        elif user_choice == 3:
            update_items()
            print()
        elif user_choice == 4:
            delete_items()
            print()
        elif user_choice == 5:
            search_items()
            print()
        elif user_choice == 6:
            calculate_total_purchases()
            print()
        elif user_choice == 7:
            print("Exiting the program!") 
            sys.exit()

if __name__ == "__main__":
    main()