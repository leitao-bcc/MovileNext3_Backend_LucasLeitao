from flask_restful import Resource, reqparse

from app.providers.ifood_provider import IfoodProvider
from app.transformers.ifood_transform import IfoodTransform


class AuthResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        data = AuthResource.parser.parse_args()

        provider = IfoodProvider()

        provider_response = provider.login(data.get('username'),
                                           data.get('password'))

        if not provider_response:
            return '', 400

        transform = IfoodTransform()

        customer = transform.transform_login(provider_response)

        if not customer:
            return '', 400

        return customer.to_json()
