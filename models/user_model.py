import json
import os

class UserModel:
    DEFAULT_PATH = 'data/users.json'

    @staticmethod
    def load_json(path=None):
        path = path or UserModel.DEFAULT_PATH
        try:
            with open(path, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("data di json error cek json")
    
    @staticmethod
    def save_json(data, path=None):

        path = path or UserModel.DEFAULT_PATH

  

        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

