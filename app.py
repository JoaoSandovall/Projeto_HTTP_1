from flask import Flask

app = Flask(__name__)

items = [
    {"id": 1, "name": "Aprender Flask"},
    {"id": 2, "name": "Construir a primeria API"},
    {"id": 3, "name": "Entender requisições HTTP"}, 
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == '__name__':
    app.run(debug=True)