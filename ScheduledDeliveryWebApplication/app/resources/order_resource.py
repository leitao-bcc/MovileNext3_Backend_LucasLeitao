from flask_restful import Resource, reqparse


class OrderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('customerId', type=str, required=True)
    parser.add_argument('merchantId', type=str, required=True)
    parser.add_argument('deliveryAddress', type=str, required=True)
    parser.add_argument('deliveryDateTime', type=str, required=True)
    parser.add_argument('items', type=str, required=True)

    def post(self):
        from app.transformers.base_transform import BaseTransform

        data = OrderResource.parser.parse_args(strict=True)

        transform = BaseTransform()

        order = transform.transform_canonic_order(data)

        if not order:
            return '', 400

        return str(order.id), 201


class OrderConfirmResource(Resource):

    def post(self, order_id):
        from app.providers.ifood_provider import IfoodProvider

        provider = IfoodProvider()

        data = {"orderId": order_id}

        return provider.post_order(**data)
