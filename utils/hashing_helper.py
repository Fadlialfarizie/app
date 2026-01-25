import bcrypt


def hashing_password(password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return password_hash

def validate_password(password, password_user):
    password = bcrypt.checkpw(password.encode('utf-8'), password_user.encode('utf-8'))
    return password