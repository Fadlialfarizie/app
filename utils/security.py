import secrets
from flask import session, request
from functools import wraps
from errors.handler import AuthError, ValidationError



def generate_csrf_tooken():
    token = secrets.token_hex(16)
    session['csrf_token'] = token
    return token


def csrf_protected(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.method in ['POST', 'PATCH', 'PUT', 'DELETE']:
            token_session = session.get('csrf_token')
            token_headers = request.headers.get('X-CSRF-Token')
            if not token_headers:
                raise AuthError('token headers kosong')
            if token_headers != token_session:
                raise ValidationError('token tidak valid')
        return f(*args, **kwargs)
    return wrapper