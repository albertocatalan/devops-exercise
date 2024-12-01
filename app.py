from flask import Flask, request, jsonify

app = Flask(__name__)

# Global counter for POST requests.
# This helps track how many POST requests we've received, which is part of the extra points for the task.
post_request_counter = 0

@app.route("/", methods=["GET"])
def hello():
    # Here, we're simply returning a "Hello, World" message, along with the current POST request counter.
    # This is useful for monitoring, so you can easily track how many POST requests we've handled.
    return jsonify({
        "message": "Hello, World!!!",
        "post_request_count": post_request_counter  # Show the POST request count here.
    })

@app.route("/", methods=["POST"])
def post_counter():
    global post_request_counter
    post_request_counter += 1  # Increment the counter every time we get a POST request.

    # Respond with a confirmation message, including the updated POST request count.
    # This helps monitor activity in real-time and ensures our service is behaving as expected.
    return jsonify({
        "message": "POST request received!",
        "post_request_count": post_request_counter  # Return the updated POST counter.
    })

if __name__ == "__main__":
    # Start the app to listen on all network interfaces on port 5000.
    # This is important for **deploy** because it allows the app to be accessed from anywhere,
    # and makes scaling easier if needed in a production environment.
    app.run(debug=True, host='0.0.0.0', port=5000)
