import json
from flask import Flask, render_template, request, redirect, flash
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_id = 4

# Home page - Show all dishes


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Add a dish


@app.route('/add', methods=['POST'])
def add_dish():
    global next_id
    name = request.form['name']
    availability = request.form['availability']
    dish = {'id': next_id, 'name': name, 'availability': availability}
    next_id += 1
    dishes.append(dish)
    return redirect('/')

# Update a dish


@app.route('/update/<int:dish_id>', methods=['POST'])
def update_dish(dish_id):
    name = request.form['name']
    availability = request.form['availability']
    for dish in dishes:
        if dish['id'] == dish_id:
            dish['name'] = name
            dish['availability'] = availability
            break
    return redirect('/')

# Remove a dish


@app.route('/delete/<int:dish_id>')
def delete_dish(dish_id):
    for dish in dishes:
        if dish['id'] == dish_id:
            dishes.remove(dish)
            break
    return redirect('/')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for orders (you can replace it with your own data source)
orders = []
next_order_id = 1

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html')

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    customer_email = request.form['customer-email']
    menu_item = request.form['menu-item']
    order_notes = request.form['order-notes']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'customer_email': customer_email,
        'menu_item': menu_item,
        'order_notes': order_notes,
        'status': 'New'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()

    from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_id = 4

# Sample data for orders (you can replace it with your own data source)
orders = []
next_order_id = 1

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    dish_names = [dish['name'] for dish in dishes]
    if dish_id not in [dish['id'] for dish in dishes]:
        return "Invalid dish ID."

    dish_name = dishes[dish_id - 1]['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'New'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()

    from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_id = 4

# Sample data for orders (you can replace it with your own data source)
orders = []
next_order_id = 1

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    dish_names = [dish['name'] for dish in dishes]
    if dish_id not in [dish['id'] for dish in dishes]:
        return "Invalid dish ID."

    # Check dish availability
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish and dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dishes[dish_id - 1]['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'New'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    if dish_id not in [dish['id'] for dish in dishes]:
        return "Invalid dish ID."

    # Check dish availability
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish and dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dish['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    if dish_id not in [dish['id'] for dish in dishes]:
        return "Invalid dish ID."

    # Check dish availability
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish and dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dish['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        return "Invalid order ID."

    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    if dish_id not in [dish['id'] for dish in dishes]:
        return "Invalid dish ID."

    # Check dish availability
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish and dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dish['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        return "Invalid order ID."

    # Find the order and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    if dish_id not in [dish['id'] for dish in dishes]:
        return "Invalid dish ID."

    # Check dish availability
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish and dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dish['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        flash("Invalid order ID.", "error")
        return redirect('/orders')

    # Find the order and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    flash("Order status updated successfully.", "success")
    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if not dish:
        return "Invalid dish ID."

    # Check dish availability
    if dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dish['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        return "Invalid order ID."

    # Find the order and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if not dish:
        return "Invalid dish ID."

    # Check dish availability
    if dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dish['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        return "Invalid order ID."

    # Find the order and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available'},
    {'id': 2, 'name': 'Burger', 'availability': 'available'},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable'}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if not dish:
        return "Invalid dish ID."

    # Check dish availability
    if dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

    dish_name = dish['name']

    order = {
        'id': next_order_id,
        'customer_name': customer_name,
        'dish_name': dish_name,
        'order_notes': order_notes,
        'status': 'received'
    }
    next_order_id += 1
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        return "Invalid order ID."

    # Validate order status
    valid_statuses = ['received', 'in progress', 'completed']
    if status not in valid_statuses:
        return "Invalid order status."

    # Find the order and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available', 'price': 10.99},
    {'id': 2, 'name': 'Burger', 'availability': 'available', 'price': 8.99},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable', 'price': 12.99}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if not dish:
        return "Invalid dish ID."

    # Check dish availability
    if dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

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
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    # Calculate total price for each order
    for order in orders:
        order['total_price'] = order['price']

    return render_template('orders.html', orders=orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        return "Invalid order ID."

    # Validate order status
    valid_statuses = ['received', 'in progress', 'completed']
    if status not in valid_statuses:
        return "Invalid order status."

    # Find the order and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

# Sample data for dishes (you can replace it with your own data source)
dishes = [
    {'id': 1, 'name': 'Pizza', 'availability': 'available', 'price': 10.99},
    {'id': 2, 'name': 'Burger', 'availability': 'available', 'price': 8.99},
    {'id': 3, 'name': 'Pasta', 'availability': 'unavailable', 'price': 12.99}
]
next_order_id = 1
orders = []

# Home page - Show order form


@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

# Process order


@app.route('/place_order', methods=['POST'])
def place_order():
    global next_order_id
    customer_name = request.form['customer-name']
    dish_id = int(request.form['dish-id'])
    order_notes = request.form['order-notes']

    # Validate customer name
    if not customer_name:
        return "Customer name is required."

    # Validate dish ID
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if not dish:
        return "Invalid dish ID."

    # Check dish availability
    if dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

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
    orders.append(order)

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    status_filter = request.args.get('status', None)
    filtered_orders = orders

    if status_filter:
        filtered_orders = [
            order for order in orders if order['status'] == status_filter]

    for order in filtered_orders:
        order['total_price'] = order['price']

    return render_template('orders.html', orders=filtered_orders)

# Update order status


@app.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    # Validate order ID
    order_ids = [order['id'] for order in orders]
    if order_id not in order_ids:
        return "Invalid order ID."

    # Validate order status
    valid_statuses = ['received', 'in progress', 'completed']
    if status not in valid_statuses:
        return "Invalid order status."

    # Find the order and update its status
    for order in orders:
        if order['id'] == order_id:
            order['status'] = status
            break

    return redirect('/orders')


if __name__ == '__main__':
    app.run()


app = Flask(__name__)

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
        return "Customer name is required."

    # Validate dish ID
    dish = next((dish for dish in menu_data if dish['id'] == dish_id), None)
    if not dish:
        return "Invalid dish ID."

    # Check dish availability
    if dish['availability'] != 'available':
        return f"The dish '{dish['name']}' is currently unavailable."

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

    return redirect('/orders')

# Show orders


@app.route('/orders')
def show_orders():
    _, orders_data = load_data()

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
        return "Invalid order ID."

    # Validate order status
    valid_statuses = ['received', 'in progress', 'completed']
    if status not in valid_statuses:
        return "Invalid order status."

    # Find the order and update its status
    for order in orders_data:
        if order['id'] == order_id:
            order['status'] = status
            break

    save_data(menu_data, orders_data)

    return redirect('/orders')


if __name__ == '__main__':
    # Load data on system startup
    menu_data, orders_data = load_data()
    next_order_id = max(order['id']
                        for order in orders_data) + 1 if orders_data else 1

    app.run()
