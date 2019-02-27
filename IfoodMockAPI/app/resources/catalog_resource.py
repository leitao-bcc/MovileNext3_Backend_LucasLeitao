from flask_restful import Resource, reqparse

json_catalog = """

"""


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
        return json_catalog
