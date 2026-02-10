import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logging(app):
    
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)


    if root_logger.handlers:
        return

    #setup handler file log
    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=10240,
        backupCount=10
    )
    

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)


    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)
    app.logger.info('logging setup complete')