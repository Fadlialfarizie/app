import secrets
from flask import Blueprint, jsonify, request, session
from services.user_service import create_data_user, validate_user
from utils.jwt_generate import generate_token_access, generate_token_refresh, login_required
from errors.handler import ValidationError
from schemas.auth_schema import RegisterSchema, LoginSchema


bp_auth = Blueprint('auth', __name__, url_prefix="/auth")
register_schema = RegisterSchema()
login_schema = LoginSchema()


@bp_auth.route('/register', methods=['POST'])
def register():
    try:
        data_request = register_schema.load(request.json)
    except ValueError as e:
        raise ValueError(e.messages) from e

    
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
    except ValidationError as e:
        raise ValidationError(e.messages)


    user = validate_user(data_request['username'], data_request['password'])


    token_access = generate_token_access(user)
    token_refresh = generate_token_refresh(user)
    token_csrf = secrets.token_hex(16)

    session['csrf_token'] = token_csrf
    

    respons = jsonify({
        'success' : True,
        'message' : 'login sukses',
        'data' : {
            'username' : user['username'],
            'role' : user['role']
        }
    })

    respons.set_cookie(
        'access_token',
        token_access,
        httponly=True,
        secure=True,
        samesite='None',
        path='/'
    )

    respons.set_cookie(
        'refresh_token',
        token_refresh,
        httponly=True,
        secure=True,
        samesite='None',
        path='/'
    )

    return respons, 200

@bp_auth.route('/logout', methods=['POST'])
def logout():
    session.clear()

    response = jsonify({
        'success' : True,
        'message' : 'logout sukses'
    })

    response.set_cookie(
        'access_token',
        '',
        httponly=True,
        secure=True,
        samesite='None',
        path='/'
    )


    response.set_cookie(
        'refresh_token',
        '',
        httponly=True,
        secure=True,
        samesite='None',
        path='/'
    )

    return response, 200