from flask import Flask
from routes.user import bp_user

app = Flask(__name__)

app.register_blueprint(bp_user)

if __name__ == '__main__':
    app.run(debug=True)
