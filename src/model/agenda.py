from flask import jsonify, request

from src.db import database

db_connection = database.get_db_connection()

def get():
    return jsonify(listAgenda)

def getBy(item_id):
    item = next((item for item in listAgenda if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

def post():
    new_item = request.json
    if not new_item or 'nome' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    new_item['id'] = len(listAgenda) + 1 
    listAgenda.append(new_item)
    return jsonify(new_item), 201

def put(item_id):
    item_data = request.json
    item = next((item for item in listAgenda if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Registro não encontrado"}), 404

def delete(item_id):
    global listAgenda # Permite modificar a lista global
    original_len = len(listAgenda)
    listAgenda = [item for item in listAgenda if item['id'] != item_id]
    if len(listAgenda) < original_len:
        return jsonify({"message": " registro deletado com sucesso"}), 200
    return jsonify({"message": "registro não encontrado"}), 404