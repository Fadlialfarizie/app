from flask import Flask
from config import Config
from extentions import init_extentions
from routes.user import bp_user
from routes.auth import bp_auth
from routes.produk import bp_produk
from errors.handler import register_error_handlers



def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)


    init_extentions(app)



    app.register_blueprint(bp_user)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_produk)

    register_error_handlers(app)


    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
