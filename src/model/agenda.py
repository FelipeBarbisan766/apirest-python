from flask import jsonify, request
# agenda
# Dados de exemplo (pode ser substituído por um banco de dados)
listAgenda = [
        {"id": 1, "nome": "jose", "celular": "16 9991-1113"},
        {"id": 2, "nome": "maria", "celular": "16-88891-9952"},
]

# Rota para obter todos 
#@app.route('/agenda', methods=['GET'])
def get():
    return jsonify(listAgenda)

# Rota para obter um item específico por ID
#@app.route('/agenda/<int:item_id>', methods=['GET'])
def getBy(item_id):
    item = next((item for item in listAgenda if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para adicionar um novo item
#@app.route('/agenda', methods=['POST'])
def post():
    new_item = request.json
    if not new_item or 'nome' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    # Atribui um novo ID (simples, para exemplo)
    new_item['id'] = len(listAgenda) + 1 
    listAgenda.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
#@app.route('/agenda/<int:item_id>', methods=['PUT'])
def put(item_id):
    item_data = request.json
    item = next((item for item in listAgenda if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Registro não encontrado"}), 404

# Rota para deletar um item
#@app.route('/agenda/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    global listAgenda # Permite modificar a lista global
    original_len = len(listAgenda)
    listAgenda = [item for item in listAgenda if item['id'] != item_id]
    if len(listAgenda) < original_len:
        return jsonify({"message": " registro deletado com sucesso"}), 200
    return jsonify({"message": "registro não encontrado"}), 404