from flask import jsonify, request, abort
from models.item import Item

# Data items
items = [
    {
        'id': 1,
        'name': 'Item 1',
        'description': 'This is the first item.'
    },
    {
        'id': 2,
        'name': 'Item 2',
        'description': 'This is the second item.'
    },
    {
        'id': 3,
        'name': 'Item 3',
        'description': 'This is the third item.'
    }
]

def get_all_items():
    return items

def get_item_by_id(item_id):
    for item in items:
        if item['id'] == item_id:
            return item
    return None

def create_item(item_data):
    item_id = len(items) + 1
    new_item = {'id': item_id, 'name': item_data['name'], 'description': item_data['description']}
    items.append(new_item)
    return new_item

def update_item(item_id, item_data):
    item = get_item_by_id(item_id)
    if item:
        item['name'] = item_data['name']
        item['description'] = item_data['description']
        return item
    return None

def delete_item(item_id):
    item = get_item_by_id(item_id)
    if item:
        items.remove(item)
        return item
    return None
