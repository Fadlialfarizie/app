import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_EXPIRES_MINUTES = int(os.getenv('JWT_EXPIRES_MINUTES', 15))


    @staticmethod
    def validate():
        required = ['SECRET_KEY', 'JWT_SECRET_KEY']

        for key in required:
            if not os.getenv(key):
                raise RuntimeError(f'{key} belum diset dienvironment')
            
