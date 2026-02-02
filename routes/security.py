from flask import Blueprint, jsonify, request,session
from errors.handler import AuthError



bp_security = Blueprint('security', __name__, url_prefix='/security')



@bp_security.route('/csrf')
def get_csrf():
    if not session['csrf_token']:
        raise AuthError('anda belum login')
    

    token_csrf = session['csrf_token']
    return jsonify({
        'success' : True,
        'message' : 'csrf token',
        'data' : token_csrf
    })

