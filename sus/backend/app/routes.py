from app import app
from flask import jsonify

@app.route('/api/example', methods=['GET'])
def get_example():
    return jsonify({"message": "Hello, World!"})