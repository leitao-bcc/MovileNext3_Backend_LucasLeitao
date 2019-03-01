from flask_restful import Resource

from app.providers.ifood_provider import IfoodProvider


class OrderResource(Resource):

    def post(self):
        pass

    def put(self, order_id):
        provider = IfoodProvider()

        return provider.post_order({})
