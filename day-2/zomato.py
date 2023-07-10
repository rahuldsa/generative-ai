import json

menu_file = "menu.json"
orders_file = "orders.json"

# Load menu data from file


def load_menu():
    try:
        with open(menu_file) as file:
            menu = json.load(file)
        return menu
    except FileNotFoundError:
        return {}

# Save menu data to file


def save_menu(menu):
    with open(menu_file, "w") as file:
        json.dump(menu, file)

# Load orders data from file


def load_orders():
    try:
        with open(orders_file) as file:
            orders = json.load(file)
        return orders
    except FileNotFoundError:
        return []

# Save orders data to file


def save_orders(orders):
    with open(orders_file, "w") as file:
        json.dump(orders, file)

# Display the menu


def display_menu(menu):
    print("Menu:")
    print("ID  | Dish Name        | Price     | Availability")
    print("-----------------------------------------------")
    for dish_id, dish in menu.items():
        print(
            f"{dish_id:<4} | {dish['name']:<16} | {dish['price']:<9} | {dish['availability']}")
    print()

# Add a new dish to the menu


def add_dish(menu):
    dish_id = input("Enter the dish ID: ")
    if dish_id in menu:
        print("Dish ID already exists. Please choose a different ID.")
        return

    dish_name = input("Enter the dish name: ")
    dish_price = float(input("Enter the dish price: "))
    dish_availability = input("Is the dish available? (yes/no): ")

    menu[dish_id] = {
        "name": dish_name,
        "price": dish_price,
        "availability": dish_availability.lower() == "yes"
    }
    print("Dish added successfully to the menu.")

# Remove a dish from the menu


def remove_dish(menu):
    dish_id = input("Enter the dish ID to remove: ")
    if dish_id not in menu:
        print("Dish ID does not exist.")
        return

    del menu[dish_id]
    print("Dish removed successfully from the menu.")

# Update the availability of a dish


def update_dish_availability(menu):
    dish_id = input("Enter the dish ID to update availability: ")
    if dish_id not in menu:
        print("Dish ID does not exist.")
        return

    dish_availability = input("Is the dish available? (yes/no): ")
    menu[dish_id]["availability"] = dish_availability.lower() == "yes"
    print("Dish availability updated successfully.")

# Take a new order


def take_order(menu, orders):
    customer_name = input("Enter the customer name: ")

    order_items = []
    while True:
        dish_id = input("Enter the dish ID (press enter to finish): ")
        if not dish_id:
            break

        if dish_id not in menu or not menu[dish_id]["availability"]:
            print("Invalid dish ID or dish not available.")
        else:
            order_items.append(dish_id)

    if not order_items:
        print("No valid dishes selected. Order not placed.")
        return

    order_id = len(orders) + 1
    order = {
        "id": order_id,
        "customer_name": customer_name,
        "items": order_items,
        "status": "received"
    }
    orders.append(order)
    print(f"Order placed successfully. Order ID: {order_id}")

# Update the status of an order


def update_order_status(orders):
    order_id = int(input("Enter the order ID to update status: "))
    for order in orders:
        if order["id"] == order_id:
            print("Current Status:", order["status"])
            new_status = input("Enter the new status: ")
            order["status"] = new_status
            print("Order status updated successfully.")
            return
    print("Order ID not found.")

# Review all orders


def review_orders(orders):
    print("All Orders:")
    for order in orders:
        print(f"Order ID: {order['id']}")
        print(f"Customer Name: {order['customer_name']}")
        print("Items:")
        for dish_id in order["items"]:
            print(f"- {menu[dish_id]['name']}")
        print(f"Status: {order['status']}")
        print()

# Main function


def main():
    menu = load_menu()
    orders = load_orders()

    while True:
        print("Zesty Zomato - Main Menu")
        print("1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Availability")
        print("5. Take New Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        print()

        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            add_dish(menu)
            save_menu(menu)
        elif choice == "3":
            remove_dish(menu)
            save_menu(menu)
        elif choice == "4":
            update_dish_availability(menu)
            save_menu(menu)
        elif choice == "5":
            take_order(menu, orders)
            save_orders(orders)
        elif choice == "6":
            update_order_status(orders)
            save_orders(orders)
        elif choice == "7":
            review_orders(orders)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    main()
