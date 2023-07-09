# Global list to store the snack inventory
snacks = []

def manage_inventory():
    print("---- Manage Inventory ----")
    print("1. Add a snack to inventory")
    print("2. Remove a snack from inventory")
    print("3. Update snack availability")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_snack_availability()
    else:
        print("Invalid choice. Please try again.")

def add_snack():
    print("---- Add Snack ----")
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    snack_price = float(input("Enter snack price: "))
    snack_availability = int(input("Enter snack availability: "))

    snack = {
        "id": snack_id,
        "name": snack_name,
        "price": snack_price,
        "availability": snack_availability
    }

    snacks.append(snack)
    print("Snack added successfully.")

def remove_snack():
    print("---- Remove Snack ----")
    snack_id = input("Enter snack ID to remove: ")

    for snack in snacks:
        if snack["id"] == snack_id:
            snacks.remove(snack)
            print("Snack removed successfully.")
            return

    print("Snack not found.")

def update_snack_availability():
    print("---- Update Snack Availability ----")
    snack_id = input("Enter snack ID: ")
    new_availability = int(input("Enter new availability: "))

    for snack in snacks:
        if snack["id"] == snack_id:
            snack["availability"] = new_availability
            print("Snack availability updated successfully.")
            return

    print("Snack not found.")

def record_sale():
    print("---- Record Sale ----")
    snack_id = input("Enter snack ID: ")

    for snack in snacks:
        if snack["id"] == snack_id:
            if snack["availability"] > 0:
                snack["availability"] -= 1
                print("Sale recorded successfully.")
            else:
                print("Snack is unavailable.")
            return

    print("Snack not found.")

def display_inventory():
    print("---- Snack Inventory ----")
    if len(snacks) == 0:
        print("Inventory is empty.")
    else:
        for snack in snacks:
            print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {snack['availability']}")

# Main loop
while True:
    print("\n---- Mumbai Munchies: The Canteen Chronicle ----")
    print("1. Manage Inventory")
    print("2. Record Sale")
    print("3. Display Inventory")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        manage_inventory()
    elif choice == "2":
        record_sale()
    elif choice == "3":
        display_inventory()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
