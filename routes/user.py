from flask import Blueprint, jsonify, request
from services.user_service import get_all_user, create_data_user, remove_user


bp_user = Blueprint('user',__name__, url_prefix='/user')

@bp_user.route('/')
def get_user():
    data_user = get_all_user()
    return jsonify({
        'success' : True,
        'message' : "success",
        'data' : data_user
    })


@bp_user.route('/', methods=['POST'])
def create_user():
    data_request = request.json
    if not data_request:
        return jsonify({
            'success' : False,
            'message' : 'request kosong'
        }), 400
    
    if not 'username' in data_request or not 'role' in data_request:
        return jsonify({
            'success' : False,
            'message' : 'nama/role tidak boleh kosong'
        }), 400
    
    
    create_data_user(data_request)

    return jsonify({
        'success' : True,
        'message' : 'user berhasil ditambahkan',
        'data' : data_request
    }), 200

@bp_user.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    remove_user(id)
    return jsonify({
        'success' : True,
        'message': 'user berhasil dihapus',
        'data' : ''
    }), 204