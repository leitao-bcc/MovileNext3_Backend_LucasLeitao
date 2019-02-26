from app import db
from app.models.base import BaseModel


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
    deliveryAddress = db.relationship('AddressModel')

    created_at = db.Column(db.DateTime, nullable=False)
    deliveryDateTime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<OrderModel %r>" % self.id
