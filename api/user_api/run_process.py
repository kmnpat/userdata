from flask_restful import Resource, reqparse
from database import Users_data



class ShowAllUser(Resource):
    def get(self):
        db = Users_data()
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('gender', type=str)
        parser.add_argument('age', type=int)

        args = parser.parse_args()
        id = args['id'] if args['id'] else ''
        first_name = args['first_name'] if args['first_name'] else ''
        last_name = args['last_name'] if args['last_name'] else ''
        email = args['email'] if args['email'] else ''
        gender = args['gender'] if args['gender'] else ''
        age = args['age'] if args['age'] else ''
        return db.all_data(id=id, first_name=first_name, last_name=last_name, email=email,
                              gender=gender, age=age)


class DeleteUser(Resource):
    def get(self):
        db = Users_data()
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)

        args = parser.parse_args()
        id = args['id'] if args['id'] else ''
        return db.delete_data(id=id)


class InsertUser(Resource):
    def get(self):
        db = Users_data()
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('gender', type=str)
        parser.add_argument('age', type=int)

        args = parser.parse_args()
        id = args['id'] if args['id'] else ''
        first_name = args['first_name'] if args['first_name'] else ''
        last_name = args['last_name'] if args['last_name'] else ''
        email = args['email'] if args['email'] else ''
        gender = args['gender'] if args['gender'] else ''
        age = args['age'] if args['age'] else ''
        return db.insert_data(id=id, first_name=first_name, last_name=last_name, email=email,
                              gender=gender, age=age)

class UpdateUser(Resource):
    def get(self):
        db = Users_data()
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('gender', type=str)
        parser.add_argument('age', type=int)

        args = parser.parse_args()
        id = args['id'] if args['id'] else ''
        first_name = args['first_name'] if args['first_name'] else ''
        last_name = args['last_name'] if args['last_name'] else ''
        email = args['email'] if args['email'] else ''
        gender = args['gender'] if args['gender'] else ''
        age = args['age'] if args['age'] else ''
        return db.update_data(id=id, first_name=first_name, last_name=last_name, email=email,
                              gender=gender, age=age)