from flask_restful import Resource


class MerchantResource(Resource):

    def get(self, merchant_id):
        from app.providers.ifood_provider import IfoodProvider
        from app.transformers.ifood_transform import IfoodTransform

        provider = IfoodProvider()

        provider_response = provider.get_merchant(merchant_id)

        if not provider_response:
            return '', 404

        transform = IfoodTransform()

        items = transform.transform_merchant(provider_response)

        if not items:
            return '', 404

        return [item.to_json() for item in items]
