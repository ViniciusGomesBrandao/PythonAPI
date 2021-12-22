from flask import Flask
from flask_restful import Api
from modules.users import Users
from modules.auth import Login

app = Flask(__name__)
api = Api(app)
api.add_resource(Users, '/users')
api.add_resource(Login, '/login')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)