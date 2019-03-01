from app.models.address_model import AddressModel
from app.models.category_model import CategoryModel
from app.models.customer_model import CustomerModel
from app.models.item_model import ItemModel
from app.models.merchant_model import MerchantModel
from app.models.office_hour_model import OfficeHourModel
from app.models.phone_model import PhoneModel
from app.transformers.base_transform import BaseTransform


class IfoodTransform(BaseTransform):

    def transform_catalog(self, data):
        merchant_list = []
        for item in data:
            try:
                merchant_obj = MerchantModel(
                    item.get('name'),
                    item.get('description'),
                    item.get('rating')
                )

                category_obj = CategoryModel(item.get('category'))
                merchant_obj.category = category_obj

                phone_list = []
                for phone_str in item.get('phones', []):
                    phone_list.append(
                        PhoneModel(phone_str[:2], phone_str[2:])
                    )
                merchant_obj.phones.add(phone_list)

                for office_hours_dict in item.get('officeHours', []):
                    office_hours_obj = OfficeHourModel(
                        office_hours_dict.get('weekDay'),
                        office_hours_dict.get('startTime'),
                        office_hours_dict.get('endTime')
                    )
                    office_hours_obj.merchant = merchant_obj

                address_dict = item.get('address', {})
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
                merchant_obj.address = address_obj

                merchant_list.append(merchant_obj)

            except ValueError:
                pass

        return merchant_list

    def transform_merchant(self, data):
        item_list = []
        for item_dict in data.get('items', []):
            try:
                item_list.append(
                    ItemModel(
                        item_dict.get('name'),
                        item_dict.get('price'),
                        item_dict.get('section')
                    )
                )
            except ValueError:
                pass
        return item_list

    def transform_login(self, data):
        try:
            customer_obj = CustomerModel(
                data.get('name'),
                data.get('taxPayerIdentificationNumber'),
                data.get('email')
            )

            phone_str = data.get('phone')
            phone_obj = PhoneModel(phone_str[:2], phone_str[2:])
            customer_obj.phone = phone_obj

            return customer_obj
        except ValueError:
            pass

        return None
