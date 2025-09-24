from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Aprender Flask"},
    {"id": 2, "name": "Construir a primeira API"},
    {"id": 3, "name": "Entender requisições HTTP"},
]

@app.route('/items', methods=['GET'])
def get_items():
    
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    last_id = [-1]["id"] if items else 0
    new_id = last_id + 1
    
    items.append({"id": new_id, "name": new_item["name"]})
    
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)