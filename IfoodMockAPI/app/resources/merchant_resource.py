from flask_restful import Resource

from app.data.merchant_data import MERCHANT_DATA


class MerchantResource(Resource):

    def get(self, merchant_id):
        MERCHANT_DATA['id'] = merchant_id
        return MERCHANT_DATA
