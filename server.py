from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]

# Helper function to get the next unique ID
def get_next_id():
    return max((event["id"] for event in events), default=0) + 1

# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201
@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()

    # Validate input
    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    new_event = {
        "id": get_next_id(),
        "title": data["title"].strip()
    }

    events.append(new_event)
    return jsonify(new_event), 201

# Optional: handle undefined routes gracefully
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
