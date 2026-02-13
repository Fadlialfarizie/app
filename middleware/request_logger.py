from flask import request
import logging
import time




def register_request_logger(app):

    @app.before_request
    def logger_request():
        request.time_request = time.time()
        logging.info(f'{request.method}, {request.path}')
    

    @app.after_request
    def logger_response(response):
        time_response = (time.time() - request.time_request) * 1000
        ip = request.remote_addr
        method = request.method
        path = request.path
        logging.info(
            f'IP: {ip} - {method} - {path} - duration : {time_response: .3f}ms'
        )
        return response