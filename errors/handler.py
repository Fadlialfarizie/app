from flask import jsonify
from werkzeug.exceptions import HTTPException




class AppError(Exception):
    def __init__(self, message, code, status_code):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(message)

class ValidationError(AppError):
    def __init__(self, message):
        super().__init__(message, code="VALIDATION_ERROR", status_code=400)


class AuthError(AppError):
    def __init__(self, message="autentication error"):
        super().__init__(message, code='AUTH_ERROR', status_code=401)

class Forbidden(AppError):
    def __init__(self, message="forbidden"):
        super().__init__(message, code="FORBIDDEN", status_code=403)


class NotFoundError(AppError):
    def __init__(self, message='resource not found'):
        super().__init__(message, code='not_found_error', status_code=404)


def register_error_handlers(app):

    @app.errorhandler(AppError)
    def handle_app_error(err):
        return jsonify({
            'success' : False,
            'message' : err.message
        }), err.status_code
    
    @app.errorhandler(HTTPException)
    def handle_http_error(err):
        return jsonify({
            'success' : False,
            'message' : err.message
        }), err.status_code
    
    @app.errorhandler(Exception)
    def handle_erro(err):
        return jsonify({
            'success' : False,
            'message' : err.message
        }), err.status_code