from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Global counter for POST requests.
# This helps track how many POST requests we've received, which is part of the extra points for the task.

# >>> Updated: Using a persistent database for the counter to ensure consistent state across multiple replicas.
DB_PATH = "/data/counter.db"

# >>> Updated: Initialize the database to store the counter persistently.
if not os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, count INTEGER)")
    cursor.execute("INSERT INTO counter (id, count) VALUES (1, 0)")  # Initialize the counter at 0.
    conn.commit()
    conn.close()

# >>> Updated: Function to fetch the current counter value from the database.
def get_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM counter WHERE id=1")
    count = cursor.fetchone()[0]
    conn.close()
    return count

# >>> Updated: Function to increment the counter value in the database.
def increment_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET count = count + 1 WHERE id=1")
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def hello():
    # Here, we're simply returning a "Hello, World" message, along with the current POST request counter.
    # This is useful for monitoring, so you can easily track how many POST requests we've handled.
    
    # >>> Updated: Fetch the counter value from the database for accurate tracking across replicas.
    return jsonify({
        "message": "Hello, World!!!",
        "post_request_count": get_count()  # Show the POST request count here.
    })

@app.route("/", methods=["POST"])
def post_counter():
    global post_request_counter
    # >>> Updated: Increment the counter in the shared database to ensure all replicas share the same state.
    increment_count()

    # Respond with a confirmation message, including the updated POST request count.
    # This helps monitor activity in real-time and ensures our service is behaving as expected.
    return jsonify({
        "message": "POST request received!",
        "post_request_count": get_count()  # Return the updated POST counter.
    })

if __name__ == "__main__":
    # Start the app to listen on all network interfaces on port 5000.
    # This is important for **deploy** because it allows the app to be accessed from anywhere,
    # and makes scaling easier if needed in a production environment.
    
    # >>> Updated: Removed debug mode for better alignment with production best practices.
    app.run(host='0.0.0.0', port=5000)
