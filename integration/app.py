from rasa import run, version
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField
from flask_wtf import FlaskForm
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'database_uri_here'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)
socketio = SocketIO(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    address = db.Column(db.String(200))
    orders = db.relationship('Order', backref='user', lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    orders = db.relationship('Order', backref='product', lazy=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    rating = db.Column(db.Integer)
    review = db.Column(db.String(200))


class DishForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])


@app.route('/menu')
def menu():
    dishes = Dish.query.all()
    feedbacks = Feedback.query.all()  # Retrieve feedback data
    return render_template('menu.html', dishes=dishes, feedbacks=feedbacks)


@app.route('/menu/add', methods=['GET', 'POST'])
def add_dish():
    form = DishForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        dish = Dish(name=name, description=description)
        db.session.add(dish)
        db.session.commit()
        return redirect(url_for('menu'))
    return render_template('add_dish.html', form=form)


@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    dishes = Dish.query.all()
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        selected_dish_ids = request.form.getlist('selected_dish_ids')

        # Create a new order
        order = Order(user_id=1, timestamp=datetime.now())
        db.session.add(order)
        db.session.commit()

        # Add order items
        for dish_id in selected_dish_ids:
            dish = Dish.query.get(dish_id)
            if dish:
                order_item = OrderItem(
                    order_id=order.id, dish_id=dish.id, quantity=1)
                db.session.add(order_item)

        # Calculate and update the total price for the order
        order.total_price = calculate_total_price(order)

        db.session.commit()

        # Redirect to the order list page or display a confirmation message
        return redirect(url_for('orders'))

    return render_template('order_form.html', dishes=dishes)


@app.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('order_list.html', orders=orders)


@app.route('/orders/<int:order_id>/update_status', methods=['POST'])
def update_order_status(order_id):
    order = Order.query.get(order_id)
    if order:
        new_status = request.form['status']
        # Validate the new status
        if new_status in ['Pending', 'In Progress', 'Completed']:
            order.status = new_status
            db.session.commit()
        else:
            flash('Invalid status selected.')
    return redirect(url_for('orders'))


@app.route('/orders/<int:order_id>/feedback', methods=['GET', 'POST'])
def order_feedback(order_id):
    order = Order.query.get(order_id)
    if request.method == 'POST':
        rating = request.form['rating']
        review = request.form['review']
        # Store the feedback in the database
        feedback = Feedback(order_id=order_id, rating=rating, review=review)
        db.session.add(feedback)
        db.session.commit()
        # Redirect to a thank-you page or display a confirmation message
        return render_template('feedback_thankyou.html')
    return render_template('order_feedback.html', order=order)


@socketio.on('connect')
def handle_connect():
    # Perform any necessary setup when a client connects
    pass


@socketio.on('disconnect')
def handle_disconnect():
    # Perform any necessary cleanup when a client disconnects
    pass


def send_order_status_update(order_id, status):
    emit('order_status_update', {
         'order_id': order_id, 'status': status}, broadcast=True)


@socketio.on('update_order_status')
def handle_update_order_status(data):
    order_id = data['order_id']
    status = data['status']
    # Update the order status in the database
    # ...
    # Send the updated order status to all connected clients
    send_order_status_update(order_id, status)


@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form['user_query']
    response = run(user_query)
    return response


def calculate_total_price(order):
    total_price = 0.0
    for item in order.items:
        total_price += item.quantity * item.dish.price
    return total_price


if __name__ == '__main__':
    socketio.run(app)
