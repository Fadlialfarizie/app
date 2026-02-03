from flask import Flask, jsonify
from config import Config
from logger.logger import setup_logging
from extensions import init_extensions
from routes.user import bp_user
from routes.auth import bp_auth
from routes.produk import bp_produk
from errors.handler import register_error_handlers



def create_app():

   
    Config.validate()

    app = Flask(__name__)
    app.config.from_object(Config)


    setup_logging(app)

    init_extensions(app)



    app.register_blueprint(bp_user)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_produk)

    register_error_handlers(app)


    return app

app = create_app()

@app.route("/")
def health_check():
    return jsonify({
        'success' : True,
        'message' : 'oke'
    }), 200

if __name__ == '__main__':
    app.run()
