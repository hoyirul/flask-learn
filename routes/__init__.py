from flask import jsonify, abort, request, Blueprint
from controllers.item_controller import get_all_items, get_item_by_id, create_item, update_item, delete_item

item_bp = Blueprint('item', __name__)

@item_bp.route('/items', methods=['GET'])
def get_items():
    items = get_all_items()
    return jsonify(items)

@item_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = get_item_by_id(item_id)
    if not item:
        abort(404)
    return jsonify(item)

@item_bp.route('/items', methods=['POST'])
def create_new_item():
    data = request.get_json()
    if 'name' not in data or 'description' not in data:
        abort(400)
    new_item = create_item(data)
    return jsonify(new_item), 201

@item_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_existing_item(item_id):
    item = get_item_by_id(item_id)
    if not item:
        abort(404)
    data = request.get_json()
    if 'name' not in data or 'description' not in data:
        abort(400)
    updated_item = update_item(item_id, data)
    return jsonify(updated_item)

@item_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_existing_item(item_id):
    item = get_item_by_id(item_id)
    if not item:
        abort(404)
    deleted_item = delete_item(item_id)
    return jsonify(deleted_item), 200