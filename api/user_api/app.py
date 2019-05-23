from flask import Flask
from flask_restful import Api, abort
from sqlalchemy import create_engine
from run_process import ShowAllUser, InsertUser, DeleteUser, UpdateUser
from flask_cors import CORS

e = create_engine('sqlite:///user.db')

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(ShowAllUser, '/users')
api.add_resource(DeleteUser, '/delete')
api.add_resource(InsertUser, '/insert')
api.add_resource(UpdateUser, '/update')

def handle_request_parsing_error(err):
    abort(422, errors=err.messages)


if __name__ == '__main__':
    app.run()