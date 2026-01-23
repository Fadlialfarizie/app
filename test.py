from utils.auth_helper import generate_token_access


uber = {
        "id": 1,
        "username": "diva",
        "password": "b'$2b$12$N36YFzBq0cin6O6HWssG9uIq5nC2lf0anD3egWHjmDEDRDecgJylm'",
        "role": "manager"
    }

print(generate_token_access(uber))