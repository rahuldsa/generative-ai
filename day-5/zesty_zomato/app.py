import json
from flask import Flask, jsonify, request

app = Flask(__name__)

menu = [
    {
        'id': 1,
        'name': 'Dish 1',
        'price': 10.0,
        'availability': True
    },
    {
        'id': 2,
        'name': 'Dish 2',
        'price': 15.0,
        'availability': False
    },
    # Add more dishes...
]


@app.route('/dishes', methods=['GET'])
def get_dishes():
    """Retrieve all dishes from the menu."""
    return jsonify(menu)


@app.route('/dishes/<int:dish_id>', methods=['GET'])
def get_dish(dish_id):
    """Retrieve a specific dish from the menu by ID."""
    dish = next((d for d in menu if d['id'] == dish_id), None)
    if dish:
        return jsonify(dish)
    else:
        return jsonify({'error': 'Dish not found.'}), 404


@app.route('/dishes', methods=['POST'])
def add_dish():
    """Add a new dish to the menu."""
    # Extract dish details from the request
    dish = {
        'id': request.json['id'],
        'name': request.json['name'],
        'price': request.json['price'],
        'availability': request.json['availability']
    }
    menu.append(dish)
    return jsonify({'message': 'Dish added successfully.'}), 201

# Implement routes for updating and deleting dishes


orders = [
    {
        'id': 1,
        'customer_name': 'John',
        'dish_ids': [1, 2],
        'status': 'received'
    },
    {
        'id': 2,
        'customer_name': 'Alice',
        'dish_ids': [3],
        'status': 'preparing'
    },
    # Add more orders...
]


@app.route('/orders', methods=['POST'])
def place_order():
    """Place a new order."""
    # Extract order details from the request
    order = {
        'id': len(orders) + 1,
        'customer_name': request.json['customer_name'],
        'dish_ids': request.json['dish_ids'],
        'status': 'received'
    }
    # Check if all ordered dishes are available
    available_dish_ids = [d['id'] for d in menu if d['availability']]
    for dish_id in order['dish_ids']:
        if dish_id not in available_dish_ids:
            return jsonify({'error': f'Dish with ID {dish_id} is not available.'}), 400
    orders.append(order)
    return jsonify({'message': 'Order placed successfully.'}), 201

# Implement routes for updating the status of an order and reviewing all orders


def calculate_order_total(dish_ids):
    """Calculate the total price of an order based on the dish IDs."""
    total = 0.0
    for dish_id in dish_ids:
        dish = next((d for d in menu if d['id'] == dish_id), None)
        if dish:
            total += dish['price']
    return total


@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders, with an optional filter by status."""
    status = request.args.get('status')
    if status:
        filtered_orders = [
            order for order in orders if order['status'] == status]
        return jsonify(filtered_orders)
    else:
        return jsonify(orders)


MENU_FILE = 'menu.json'
ORDERS_FILE = 'orders.json'


def load_data():
    """Load the menu and order data from JSON files."""
    with open(MENU_FILE, 'r') as f:
        menu = json.load(f)
    with open(ORDERS_FILE, 'r') as f:
        orders = json.load(f)


def save_data():
    """Save the menu and order data to JSON files."""
    with open(MENU_FILE, 'w') as f:
        json.dump(menu, f, indent=4)
    with open(ORDERS_FILE, 'w') as f:
        json.dump(orders, f, indent=4)

# Call load_data() at the beginning of your Flask application

# Call save_data() whenever there are changes to the menu or orders
