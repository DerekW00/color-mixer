from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple test route
@app.route('/')
def home():
    return "Welcome to the Acrylic Color Mixing Assistant!"

# Endpoint for adding a paint to your palette
@app.route('/api/add_paint', methods=['POST'])
def add_paint():
    data = request.json
    # You can handle storing the paint in a file or database here
    return jsonify({"message": f"Paint {data['name']} added successfully!"})

# Endpoint for getting mixing instructions
@app.route('/api/mixing_guide', methods=['POST'])
def get_mixing_guide():
    # This is where you'll integrate GPT-4 later
    return jsonify({"message": "Mixing guide will go here!"})

if __name__ == '__main__':
    app.run(debug=True)