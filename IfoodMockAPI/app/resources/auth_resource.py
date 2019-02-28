from flask_restful import Resource, reqparse

from app.data.auth_data import AUTH_DATA


class AuthResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        return AUTH_DATA
