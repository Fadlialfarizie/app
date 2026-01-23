from flask import Flask
from config import Config
from extentions import init_extentions
from routes.user import bp_user
from routes.auth import bp_auth


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    init_extentions(app)

    app.register_blueprint(bp_user)
    app.register_blueprint(bp_auth)


    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
