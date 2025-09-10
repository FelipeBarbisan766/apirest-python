from flask import jsonify, request

# usuarios
# Dados de exemplo (pode ser substituído por um banco de dados)
listUsers = [
        {"id": 1, "login": "jose", "password": "123"},
        {"id": 2, "login": "maria", "password": "123"},
]


# Rota para obter todos os itens
#@app.route('/users', methods=['GET'])
def get():
    return jsonify(listUsers)

# Rota para obter um item específico por ID
#@app.route('/users/<int:item_id>', methods=['GET'])
def getBy(item_id):
    item = next((item for item in listUsers if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para adicionar um novo item
#@app.route('/users', methods=['POST'])
def post():
    new_item = request.json
    if not new_item or 'login' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    # Atribui um novo ID (simples, para exemplo)
    new_item['id'] = len(listUsers) + 1 
    listUsers.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
#@app.route('/users/<int:item_id>', methods=['PUT'])
def put(item_id):
    item_data = request.json
    item = next((item for item in listUsers if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para deletar um item
#@app.route('/users/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    global listUsers # Permite modificar a lista global
    original_len = len(listUsers)
    listUsers = [item for item in listUsers if item['id'] != item_id]
    if len(listUsers) < original_len:
        return jsonify({"message": "Item deletado com sucesso"}), 200
    return jsonify({"message": "Item não encontrado"}), 404
