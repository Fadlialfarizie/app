from flask import Flask
from flask_cors import CORS


def init_extentions(app: Flask):
    CORS.init_app(app, origins=["http://localhost:*"])


