class Snack:
    def __init__(self, snack_id, snack_name, price, availability):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.availability = availability
        self.quantity_sold = 0

class CanteenInventory:
    def __init__(self):
        self.inventory = []

    def add_snack(self, snack_id, snack_name, price, availability):
        snack = Snack(snack_id, snack_name, price, availability)
        self.inventory.append(snack)
        print("Snack added to inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print("Snack removed from inventory.")
                return
        print("Snack not found in inventory.")

    def update_snack_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print("Snack availability updated.")
                return
        print("Snack not found in inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    snack.quantity_sold += 1
                    print("Snack sold.")
                    return
                else:
                    print("Snack is not available for sale.")
                    return
        print("Snack not found in inventory.")

    def get_snack_by_id(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                return snack
        return None

    def get_total_sales(self):
        total_sales = 0
        for snack in self.inventory:
            total_sales += snack.quantity_sold * snack.price
        return total_sales


# Usage example
canteen = CanteenInventory()

# Add snacks to the inventory
canteen.add_snack(1, "Chips", 10, "yes")
canteen.add_snack(2, "Cookies", 20, "yes")
canteen.add_snack(3, "Candy", 5, "no")

# Sell snacks
canteen.sell_snack(1)  # Snack sold.
canteen.sell_snack(1)  # Snack sold.
canteen.sell_snack(2)  # Snack sold.
canteen.sell_snack(3)  # Snack is not available for sale.

# Update snack availability
canteen.update_snack_availability(1, "no")

# Remove a snack
canteen.remove_snack(2)

# Get total sales
print("Total sales:", canteen.get_total_sales())
