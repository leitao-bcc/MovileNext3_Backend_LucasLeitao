from datetime import datetime

from app import db
from app.models.base_model import BaseModel
from app.validators.datetime_validator import is_valid_datetime_format


class OrderModel(db.Model, BaseModel):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'),
                            nullable=False)
    customer = db.relationship('CustomerModel')

    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'),
                            nullable=False)
    merchant = db.relationship('MerchantModel')

    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'),
                           nullable=False)
    delivery_address = db.relationship('AddressModel')

    created_at = db.Column(db.DateTime, nullable=False)
    delivery_date_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, delivery_datetime):
        if not is_valid_datetime_format(delivery_datetime):
            raise ValueError(
                "Order DeliveryDatetime {}".format(delivery_datetime))

        self.delivery_date_time = delivery_datetime
        self.created_at = datetime.now()

    def __repr__(self):
        return "<OrderModel %r>" % self.id
