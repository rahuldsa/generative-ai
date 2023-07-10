import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app = Flask(__name__, template_folder='path/to/templates')
app.config['SECRET_KEY'] = 'secret_key'  # Replace with your own secret key
socketio = SocketIO(app)

# Store connected clients
clients = set()

# Function to send order status updates to connected clients


def send_order_status_update(order_id, status):
    message = {'orderId': order_id, 'status': status}
    socketio.emit('order_status_update', message, json=True)

# Handle WebSocket connection


@socketio.on('connect')
def handle_connect():
    clients.add(request.sid)

# Remove client from connected clients set on disconnect


@socketio.on('disconnect')
def handle_disconnect():
    clients.remove(request.sid)

# Route for rendering the HTML template


@app.route('/')
def index():
    return render_template('index.html')

# Simulate order status updates (for demonstration purposes)


def simulate_order_status_updates():
    import time
    while True:
        order_id = 'ABC123'  # Replace with actual order ID
        status = 'Preparing'  # Replace with actual order status

        # Send the order status update to connected clients
        send_order_status_update(order_id, status)

        time.sleep(5)  # Interval for simulated updates in seconds


if __name__ == '__main__':
    # Start the Flask development server with SocketIO support
    socketio.run(app, debug=True)


# Define a dictionary of intents and their corresponding responses
intents = {
    "greeting": ["Hello!", "Hi there!", "Welcome! How can I assist you?"],
    "farewell": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "Glad I could help!", "Anytime!"],
    "default": ["I'm sorry, I didn't understand. Can you please rephrase?", "I'm still learning. Can you provide more information?"]
}

# Function to recognize the intent of a user query


def recognize_intent(query):
    # Convert the query to lowercase for case-insensitive matching
    query = query.lower()

    # Perform intent recognition based on keywords in the query
    if "hello" in query or "hi" in query:
        return "greeting"
    elif "goodbye" in query or "bye" in query:
        return "farewell"
    elif "thank" in query:
        return "thanks"
    else:
        return "default"

# Function to generate a response based on the recognized intent


def generate_response(intent):
    # Select a random response from the list of responses for the given intent
    response = random.choice(intents.get(intent, intents["default"]))
    return response


# Chatbot interaction loop
while True:
    user_query = input("User: ")

    # Recognize the intent of the user query
    intent = recognize_intent(user_query)

    # Generate a response based on the recognized intent
    bot_response = generate_response(intent)

    print("Bot: " + bot_response)
