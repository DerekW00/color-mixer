from flask import Flask, jsonify, request
import os
import openai
app = Flask(__name__)

# Load the OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError(
        "No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")


@app.route('/')
def home():
    return "Welcome to the Acrylic Color Mixing Assistant!"

# Endpoint for adding to palette


@app.route('/api/add_paint', methods=['POST'])
def add_paint():
    data = request.json
    # TODO: store the paint in a file or database here
    return jsonify({"message": f"Paint {data['name']} added successfully!"})

# Endpoint for getting mixing instructions


@app.route('/api/mixing_guide', methods=['POST'])
def get_mixing_guide():
    # TODO: Integrate GPT-4 later
    return jsonify({"message": "Mixing guide will go here!"})


if __name__ == '__main__':
    app.run(debug=True)
