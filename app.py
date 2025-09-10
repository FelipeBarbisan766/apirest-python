from flask import Flask, jsonify, request
from src.model.agenda import ( get_agenda  )
from src.model.users import ( get_users)

from src.model import agenda , users , items

app = Flask(__name__)

route_map = {
    'agenda': agenda,
    'users': users,
    'produtos': items,
}

# @app.route('/<resource>/auth', methods=['POST'])
# def auth(resource):
#     return users.auth()

@app.route('/<resource>', methods=['GET' , 'POST'])
@app.route('/<resource>/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_request(resource, id=None):
    if resource in route_map:
        if request.method == 'GET':
            if id is not None:
                return route_map[resource](id).getBy(id)
            return route_map[resource].get()
            
        elif request.method == 'POST':
            return route_map[resource].post()
        elif request.method == 'PUT' and id is not None:
            return route_map[resource](id).put(request.args.get(id))
        elif request.method == 'DELETE' and id is not None:
            return route_map[resource](id).delete(request.args.get(id))
    return jsonify({'error': 'Resource not found'}), 404


if __name__ == '__main__':
    app.run(debug=True) # debug=True para desenvolvimento
