from flask import Flask
from flask_cors import CORS



cors = CORS()

def init_extensions(app: Flask):
    cors.init_app(app,
                  supports_credentials=True,
                  origins=["http://localhost:8158","http://localhost:8159","http://localhost:8160"]
                    )


