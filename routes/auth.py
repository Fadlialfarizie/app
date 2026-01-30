from flask import Blueprint, jsonify, request, abort
from services.user_service import create_data_user, validate_user
from utils.jwt_generate import generate_token_access, generate_token_refresh
from errors.handler import ValidationError
from schemas.auth_schema import RegisterSchema, LoginSchema


bp_auth = Blueprint('auth', __name__, url_prefix="/auth")
register_schema = RegisterSchema()
login_schema = LoginSchema


@bp_auth.route('/register', methods=['POST'])
def register():
    try:
     data_request = register_schema(request.json)
    except Exception as e:
        raise ValueError(e)

    
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
    try:
        data_request = login_schema.load(request.json)
    except ValueError as e:
        raise ValueError(e.messages) from e


    if not 'username' in data_request or not 'password' in data_request:
        raise ValidationError('username/password salah')
    
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