import json

menu = []  # List to store the menu items


def load_menu():
    """Load the menu from a file."""
    global menu
    try:
        with open("menu.json", "r") as file:
            menu = json.load(file)
    except FileNotFoundError:
        menu = []


def save_menu():
    """Save the menu to a file."""
    with open("menu.json", "w") as file:
        json.dump(menu, file)


def add_dish():
    """Add a new dish to the menu."""
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    price = float(input("Enter dish price: "))
    availability = True
    dish = {"id": dish_id, "name": dish_name, "price": price, "availability": availability}
    menu.append(dish)
    print("Dish added successfully!")


def remove_dish():
    """Remove a dish from the menu."""
    dish_id = input("Enter dish ID to remove: ")
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            print("Dish removed successfully!")
            return
    print("Dish not found in the menu!")


def update_dish_availability():
    """Update the availability of a dish."""
    dish_id = input("Enter dish ID to update availability: ")
    for dish in menu:
        if dish["id"] == dish_id:
            availability = input("Enter availability (True/False): ").lower()
            dish["availability"] = availability == "true"
            print("Dish availability updated successfully!")
            return
    print("Dish not found in the menu!")


def display_menu():
    """Display the menu to the staff."""
    print("Menu:")
    for dish in menu:
        print(f"Dish ID: {dish['id']}, Dish Name: {dish['name']}, Price: {dish['price']}, "
              f"Availability: {dish['availability']}")


def main_menu():
    """Display the main menu options."""
    print("\nWelcome to Zesty Zomato!")
    print("1. Add a new dish")
    print("2. Remove a dish")
    print("3. Update dish availability")
    print("4. Take new orders")
    print("5. Update order status")
    print("6. Review all orders")
    print("7. Exit")


def zesty_zomato():
    """The main function to run the Zesty Zomato command-line system."""
    load_menu()

    while True:
        main_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_dish()
        elif choice == "2":
            remove_dish()
        elif choice == "3":
            update_dish_availability()
        elif choice == "4":
            take_new_order()
        elif choice == "5":
            update_order_status()
        elif choice == "6":
            review_all_orders()
        elif choice == "7":
            save_menu()
            print("Thank you for using Zesty Zomato!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the Zesty Zomato system
zesty_zomato()

orders = []  # List to store the orders


def take_new_order():
    """Take a new order from the customer."""
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
    order_dishes = []

    for dish_id in dish_ids:
        dish = next((dish for dish in menu if dish["id"] == dish_id.strip()), None)
        if dish:
            if dish["availability"]:
                order_dishes.append(dish)
            else:
                print(f"Dish ID: {dish_id} is not available!")
                return
        else:
            print(f"Dish ID: {dish_id} not found!")
            return

    order_id = len(orders) + 1
    order = {"id": order_id, "customer_name": customer_name, "dishes": order_dishes, "status": "received"}
    orders.append(order)
    print(f"Order placed successfully! Order ID: {order_id}")


def update_order_status():
    """Update the status of an order."""
    order_id = int(input("Enter order ID to update status: "))
    for order in orders:
        if order["id"] == order_id:
            print(f"Current Status: {order['status']}")
            new_status = input("Enter new status: ")
            order["status"] = new_status
            print("Order status updated successfully!")
            return
    print("Order not found!")


def review_all_orders():
    """Review all the orders."""
    print("All Orders:")
    for order in orders:
        print(f"Order ID: {order['id']}, Customer Name: {order['customer_name']}, Status: {order['status']}")
        print("Dishes:")
        for dish in order["dishes"]:
            print(f"Dish ID: {dish['id']}, Dish Name: {dish['name']}, Price: {dish['price']}")
        print()


# Update the zesty_zomato function to call the new order management functions
def zesty_zomato():
    """The main function to run the Zesty Zomato command-line system."""
    load_menu()

    while True:
        main_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_dish()
        elif choice == "2":
            remove_dish()
        elif choice == "3":
            update_dish_availability()
        elif choice == "4":
            take_new_order()
        elif choice == "5":
            update_order_status()
        elif choice == "6":
            review_all_orders()
        elif choice == "7":
            save_menu()
            print("Thank you for using Zesty Zomato!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the Zesty Zomato system
zesty_zomato()
