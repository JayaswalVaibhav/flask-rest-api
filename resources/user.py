import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="cannot be blank")
        parser.add_argument('password', type=str, required=True, help="cannot be blank")
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User with that username already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        # # null coz id is auto incrementing
        # query = "INSERT INTO users VALUES (NULL,?,?)"
        # cur.execute(query, (data['username'], data['password']))
        #
        # conn.commit()
        # conn.close()

        return {'message': "User created successfully."}, 201
