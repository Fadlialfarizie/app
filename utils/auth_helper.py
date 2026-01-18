import jwt
from functools import wraps
from datetime import datetime, timedelta

SECRET_KEY = 'rasiah'

def generate_token_access(user):
    payload = {
        'username': user['id'],
        "sub" : str(user['id']),
        'role': user['role'],
        'type' : 'access',
        'exp' : datetime.utcnow() + timedelta(minutes=15)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])