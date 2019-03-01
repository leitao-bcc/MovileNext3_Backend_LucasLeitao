from flask_restful import Resource, reqparse

import app.transformers as transformers
from app.providers.ifood_provider import IfoodProvider


class CatalogResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('country', type=str, required=True)
    parser.add_argument('state', type=str, required=True)
    parser.add_argument('city', type=str, required=True)
    parser.add_argument('neighborhood', type=str, required=True)
    parser.add_argument('streetName', type=str, required=True)
    parser.add_argument('streetNumber', type=str, required=True)
    parser.add_argument('postalCode', type=str, required=True)
    parser.add_argument('complement', type=str, required=True)
    parser.add_argument('latitude', type=str, required=True)
    parser.add_argument('longitude', type=str, required=True)
    parser.add_argument('deliveryDateTime', type=str, required=True)

    def post(self):
        data = CatalogResource.parser.parse_args()

        provider = IfoodProvider()

        provider_response = provider.get_catalog(**data)

        if not provider_response:
            return '', 404

        transform = transformers.ifood_transform.IfoodTransform()

        merchant_list = transform.transform_catalog(provider_response)

        return merchant_list
