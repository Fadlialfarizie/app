import jwt
from flask import current_app, request, abort, g
from uuid import uuid4
from errors.handler import ValidationError, AuthError, Forbidden
from functools import wraps
from datetime import datetime, timedelta


def generate_token_access(user):
    payload = {
        "sub" : str(user['id']),
        'username': user['username'],
        'role': user['role'],
        'type' : 'access',
        'exp' : datetime.utcnow() + timedelta(minutes=current_app.config['JWT_EXPIRES_MINUTES'])
    }

    token = jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return token

def generate_token_refresh(user):
    payload = {
        'sub': str(user['id']),
        'jti': str(uuid4()),
        'type': 'refresh',
        'exp' : datetime.utcnow() + timedelta(days=7)
    }

    token = jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return token

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token_cookies = request.cookies.get('access_token')

        if not token_cookies:
            raise AuthError('belum login')

        try:
            g.user = jwt.decode(token_cookies, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError as e:
            raise AuthError("token expired") from e
        except jwt.InvalidTokenError as e:
            raise AuthError('token invalid') from e
        return f(*args, **kwargs)
    return wrapper


def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.cookies.get('access_token')
            if not token:
                raise AuthError("token kosong")
            try:
                payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            except jwt.ExpiredSignatureError as e:
                raise AuthError('token expired') from e
            except jwt.InvalidTokenError as e:
                raise AuthError('token inevalid') from e
            if payload['type'] != 'access':
                raise AuthError('token tidak valid')
            if payload['role'] != role:
                raise Forbidden('tidak mendapat izin')
            
            return f(*args, **kwargs)
            
        return wrapper
    return decorator