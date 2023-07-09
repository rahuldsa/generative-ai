import json
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

MENU_FILE = "menu.json"
ORDERS_FILE = "orders.json"

# Load menu and orders data from files


def load_data():
    try:
        with open(MENU_FILE, 'r') as menu_file:
            menu_data = json.load(menu_file)
    except FileNotFoundError:
        menu_data = []

    try:
        with open(ORDERS_FILE, 'r') as orders_file:
            orders_data = json.load(orders_file)
    except FileNotFoundError:
        orders_data = []

    return menu_data, orders_data

# Save menu and orders data to files


def save_data(menu_data, orders_data):
    with open(MENU_FILE, 'w') as menu_file:
        json.dump(menu_data, menu_file, indent=4)

    with open(ORDERS_FILE, 'w') as orders_file:
        json.dump(orders_data, orders_file, indent=4)

# Home page - Show order form


@app.route('/')
def index():
    menu_data, _ = load_data()
    return render_template('index.html', dishes=menu_data)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    menu_data, orders_data = load_data()

    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        flash("Customer name is required.", "error")
        return redirect('/')

    # Validate dish ID
    dish = next((dish for dish in menu_data if dish['id'] == dish_id), None)
    if not dish:
        flash("Invalid dish ID.", "error")
        return redirect('/')

    # Check dish availability
    if dish['availability'] != 'available':
        flash(f"The dish '{dish['name']}' is currently unavailable.", "error")
        return redirect('/')

    dish_name = dish['name']
    dish_price = dish['price']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received',
        'price': dish_price
    }
    next_order_id += 1
    orders_data.append(order)

    save_data(menu_data, orders_data)

    flash("Order placed successfully.", "success")
    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    menu_data, orders_data = load_data()

    status_filter = request.args.get('status', None)
    filtered_orders = orders_data

    if status_filter:
        filtered_orders = [
            order for order in orders_data if order['status'] == status_filter]

    for order in filtered_orders:
        order['total_price'] = order['price']

    return render_template('orders.html', orders=filtered_orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    menu_data, orders_data = load_data()

    # Validate order ID
    order_ids = [order['id'] for order in orders_data]
    if order_id not in order_ids:
        flash("Invalid order ID.", "error")
        return redirect('/orders')

    # Validate order status
    valid_statuses = ['received', 'in progress', 'completed']
    if status not in valid_statuses:
        flash("Invalid order status.", "error")
        return redirect('/orders')

    # Find the order and update its status
    for order in orders_data:
        if order['id'] == order_id:
            order['status'] = status
            break

    save_data(menu_data, orders_data)

    flash("Order status updated successfully.", "success")
    return redirect('/orders')


if __name__ == '__main__':
    # Load data on system startup
    menu_data, orders_data = load_data()
    next_order_id = max(order['id']
                        for order in orders_data) + 1 if orders_data else 1

    app.run()
