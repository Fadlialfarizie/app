import jwt
from flask import current_app, request, abort, g
from utils.exception_custom import TokenExpirederror
from uuid import uuid4
from functools import wraps
from datetime import datetime, timedelta


def generate_token_access(user):
    payload = {
        'username': user['id'],
        "sub" : str(user['id']),
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

def required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token_cookies = request.cookies.get('access_token')

        if not token_cookies:
            abort(401, "login dulu")

        try:
            g.user = jwt.decode(token_cookies, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError as e:
            raise TokenExpirederror("token exoired") from e
        except jwt.InvalidTokenError as e:
            raise jwt.InvalidTokenError('token invalid') from e
        return f(*args, **kwargs)
    return wrapper

