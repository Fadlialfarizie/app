import os
from dotenv import load_dotenv

load_dotenv()

class config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_EXPIRES_MINUTES = int(os.getenv('JWT_EXPIRES_MINUTES'))


    @staticmethod
    def validate():
        required = ['SECRET_KEY', 'JWT_SECRET_KEY', 'JWT_EXPIRES_MINUTES']

        for key in required:
            if not os.getenv(key):
                raise RuntimeError(f'{key} belum diset dienvironment')
            
