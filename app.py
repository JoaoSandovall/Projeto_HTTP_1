from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SUA_SENHA_AQUI@localhost:5432/meu_primeiro_banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    def __init__(self, name):
        self.nome = name
        
    def to_json(self):
        return {
            "id": self.id,
            "name": self.nome
        }

@app.cli.command("create-db")
def create_tables():
    
    db.create_all()
    print("Tabelas do banco de dados criados com sucesso.")

@app.route('/items', methods=['GET'])
def get_items():

    items = ItemModel.query.all()
    return jsonify({item.to_json() for item in items})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    
    item = ItemModel.query.get_or_404(item_id)
    return jsonify(item.to_json())

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"message": "Dados inválidos: 'name' é obrigatório"}), 400
    
    new_item = ItemModel(name=data["name"])
    
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify(new_item.to_json()), 201

# ROTA: Update
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"message": "Dados inválidos: 'name' é obrigatório"}), 400
    
    item = ItemModel.query.get_or_404(item_id)
    db.session.commit()
    
    return jsonify({item.to_json()})

# Rota: DELETE
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_items(item_id):
    
    item = ItemModel.query.get_or_404(item_id)
    
    db.session.delete(item)
    db.session.commit()
    
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)