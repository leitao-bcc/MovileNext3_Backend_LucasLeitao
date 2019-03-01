from flask_restful import Resource

import app.transformers as transformers
from app.providers.ifood_provider import IfoodProvider


class MerchantResource(Resource):

    def get(self, merchant_id):
        provider = IfoodProvider()

        provider_response = provider.get_merchant(merchant_id)

        if not provider_response:
            return '', 404

        transform = transformers.ifood_transform.IfoodTransform()

        merchant = transform.transform_merchant(provider_response)

        if not merchant:
            return '', 404

        return merchant.json()
