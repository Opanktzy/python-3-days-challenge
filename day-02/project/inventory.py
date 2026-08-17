inventory = {"Soap": 10}
list_items = []

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    inventory[name] = quantity
    print(f"{name} added to inventory.")
    list_items.append(name)

def remove_item():
    name = input("Enter item name to remove: ")
    if name in inventory:
        del inventory[name]
        list_items.remove(name)
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} not found in inventory.")

def update_item():
    name = input("Enter item name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print(f"{name} updated in inventory.")
    else:
        print(f"{name} not found in inventory.")

def search_item():
    name = input("Enter item name to search: ")
    if name in inventory:
        print(f"{name} found in inventory.")
    else:
        print(f"{name} not found in inventory.")

def calculate_total_inventory_value():
    total = 0
    for name, quantity in inventory.items():
        total += quantity
    print(f"Total inventory value: {total}")

def search_item_by_lowest_stock():
    if not inventory:
        print("Inventory is empty.")
        return
    lowest_stock = min(inventory.values())
    for name, quantity in inventory.items():
        if quantity == lowest_stock:
            print(f"{name} has the lowest stock: {quantity}")
            return
    print("No item found with the lowest stock.")

def search_item_by_price():
    if not inventory:
        print("Inventory is empty.")
        return
    price = float(input("Enter the price: "))
    for name, quantity in inventory.items():
        if quantity * price == price:
            print(f"{name} has the lowest stock: {quantity}")
            return
    print("No item found with the lowest stock.")

def show_all_items():
    if not inventory:
        print("Inventory is empty.")
        return
    for name, quantity in inventory.items():
        print(f"{name}: {quantity}")


def main():
    while True:
        print("=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Search Item")
        print("5. Show All Item")
        print("6. Search Item by Lowest Stock")
        print("7. Search Item by Price")
        print("8. Calculate the total inventory value.")
        print("9. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 9:
                break
            if choice < 1 or choice > 9:
                print("Invalid choice. Please enter a number between 1 and 9.")
                continue

            if choice == 1:
                add_item()
            elif choice == 2:
                remove_item()
            elif choice == 3:
                update_item()
            elif choice == 4:
                search_item()
            elif choice == 5:
                show_all_items()
            elif choice == 6:
                search_item_by_lowest_stock()
            elif choice == 7:
                search_item_by_price()
            elif choice == 8:
                calculate_total_inventory_value()
        except ValueError:
            print("Invalid input. Please enter a number.")
main()
