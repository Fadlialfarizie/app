from flask import Blueprint, jsonify, request, abort
from services.user_service import create_data_user, validate_user
from utils.jwt_generate import generate_token_access, generate_token_refresh


bp_auth = Blueprint('auth', __name__, url_prefix="/auth")


@bp_auth.route('/register', methods=['POST'])
def register():
    data_request = request.json

    if not data_request:
        abort(401, "data request kosong")
    
    required_fields = ('username', 'password', 'role')

    if not all(field in data_request for field in required_fields):
        abort(400, 'form harus lengkap')

    create_data_user(data_request)

    return jsonify({
        'success' : True,
        'message' : 'register berhasil',
        'data' : {
            'username' : data_request['username'],
            'role' : data_request['role']
        }
    })
    

@bp_auth.route('/login', methods=['POST'])
def login():
    data_request = request.json

    if not data_request:
        abort(401, "data request kosong")

    if not 'username' in data_request or not 'password' in data_request:
        abort(401, 'username/password wajib diisi')
    
    user = validate_user(data_request['username'], data_request['password'])


    token_access = generate_token_access(user)
    token_refresh = generate_token_refresh(user)

    

    respons = jsonify({
        'success' : True,
        'message' : 'login sukses',
        'data' : user
    })

    respons.set_cookie(
        'access_token',
        token_access,
        httponly=True,
        secure=False,
        samesite='Lax'
    )
    return respons, 200

@bp_auth.route('/logout', methods=['POST'])
def logout():
    pass