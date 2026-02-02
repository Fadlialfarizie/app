import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logging(app):
    
    if not os.path.exists('logs'):
        os.makedirs('logs')
    

    if app.logger.handlers:
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

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('logging setup complete')