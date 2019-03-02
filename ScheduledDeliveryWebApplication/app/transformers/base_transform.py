import json

from app.models.address_model import AddressModel
from app.models.order_item import OrderItemModel
from app.models.order_model import OrderModel


class BaseTransform:

    def transform_catalog(self, data):
        raise NotImplementedError()

    def transform_merchant(self, data):
        raise NotImplementedError()

    def transform_login(self, data):
        raise NotImplementedError()

    def transform_canonic_order(self, data):
        try:
            order_obj = OrderModel(data.get('deliveryDateTime'))

            customer_id = data.get('customerId')
            order_obj.customer_id = customer_id

            merchant_id = data.get('merchantId')
            order_obj.merchant_id = merchant_id

            address_string = data.get('deliveryAddress', {})
            address_dict = json.loads(address_string.replace('\'', '"'))

            address_obj = AddressModel(
                address_dict.get('country'),
                address_dict.get('state'),
                address_dict.get('city'),
                address_dict.get('neighborhood'),
                address_dict.get('streetName'),
                address_dict.get('streetNumber'),
                address_dict.get('postalCode'),
                address_dict.get('complement'),
                address_dict.get('latitude'),
                address_dict.get('longitude'),
            )
            order_obj.delivery_address = address_obj

            item_string = data.get('items')
            item_dict = json.loads(item_string.replace('\'', '"'))
            item_obj = OrderItemModel(
                item_dict.get('name'),
                item_dict.get('price'),
                item_dict.get('discount'),
                item_dict.get('quantity'),
                item_dict.get('addition'),
                item_dict.get('observations'),
            )
            item_obj.oder = order_obj

            order_obj.save_to_db()

            return order_obj
        except ValueError:
            pass

        return None
