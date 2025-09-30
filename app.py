from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Aprender Flask"},
    {"id": 2, "name": "Construir a primeira API"},
    {"id": 3, "name": "Entender requisições HTTP"},
]

@app.route('/items', methods=['GET'])
def get_items():

    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    
    for item in items:
        if item["id"] == item_id:
    
            return jsonify(item)
    
    
    return jsonify({"message": "Item não encontrado"}), 404



@app.route('/items', methods=['POST'])
def add_item():
    new_item_data = request.get_json()
    
    if not new_item_data or 'name' not in new_item_data:
        return jsonify({"message": "Dados inválidos: 'name' é obrigatório"}), 400
        
    last_id = items[-1]["id"] if items else 0
    new_id = last_id + 1
    
    new_item = {"id": new_id, "name": new_item_data["name"]}
    
    items.append(new_item)
    
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    update_data = request.get_json()
    
    if not update_data or 'name' not in update_data:
        return jsonify({"message": "Dados inválidos: 'name' é obrigatório."}), 400
    
    for item in items:
        if item["id"] == item_id:
            item["name"] = update_data["name"]
            return jsonify(item)
    return jsonify({"message", "Item não encontrado"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_items(item_id):
    global items
    initial_length = len(items)
    items[:] = [item for item in items if item["id"] != item_id]
    
    if len(items) < initial_length:
        return '', 204
    else:
        return jsonify({"message": "Item não encontrado para deletar"}), 404

if __name__ == '__main__':
    app.run(debug=True)