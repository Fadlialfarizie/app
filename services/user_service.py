from models.user_model import UserModel
import bcrypt


def get_all_user():
    return UserModel.load_json()

def get_user_by_name(name):
    data_user = get_all_user()
    user = next((i for i in data_user if name == i['username']), None)
    if not user:
        raise ValueError("user tidak ditemukan")
    return user


def get_user_by_id(id):
    data_user = get_all_user()
    user = next((i for i in data_user if i['id'] == id), None)

    if not user:
        raise ValueError('user tidak ditemukan')
    
    return user


def validate_user(username, password):
    data_user = get_all_user()
    user = next((i for i in data_user if username == i['username'] and password == i['password']), None)
    if not user:
        raise ValueError("user tidak ditemukan")
    return user

def create_data_user(data_request):
    data_user = get_all_user()
    data_request = data_request

    if not data_user:
        id = 1
    else:
        id = max(i['id'] for i in data_user) + 1
    

    password = data_request['password']

    if len(password) < 8:
        raise ValueError('password minimal 8 karakter')

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = {
        'id' : id,
        'username' : data_request['username'],
        'password' : str(password_hash),
        'role' : data_request['role']
    }
    
    data_user.append(new_user)
    UserModel.save_json(data_user)



def remove_user(id):
    data_user = get_all_user()
    after_remove = next(i for i in data_user if i['id'] != id)
    UserModel.save_json(after_remove)