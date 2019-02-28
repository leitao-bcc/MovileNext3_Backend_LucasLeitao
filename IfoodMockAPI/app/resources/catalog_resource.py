from flask_restful import Resource, reqparse

from app.data.catalog_data import CATALOG_DATA


class CatalogResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('country', type=str, required=True)
    parser.add_argument('state', type=str, required=True)
    parser.add_argument('city', type=str, required=True)
    parser.add_argument('neighborhood', type=str, required=True)
    parser.add_argument('street_name', type=str, required=True)
    parser.add_argument('street_number', type=str, required=True)
    parser.add_argument('postal_code', type=str, required=True)
    parser.add_argument('complement', type=str, required=True)
    parser.add_argument('latitude', type=str, required=True)
    parser.add_argument('longitude', type=str, required=True)

    def post(self):
        return CATALOG_DATA
