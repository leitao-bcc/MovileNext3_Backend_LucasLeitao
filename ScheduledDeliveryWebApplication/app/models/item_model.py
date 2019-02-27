from app import db
from app.models.base_model import BaseModel
from app.validators.none_or_empty_validator import is_none_or_empty
from app.validators.string_format_validator import is_integer


class ItemModel(db.Model, BaseModel):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(45), nullable=False)

    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'),
                            nullable=False)
    merchant = db.relationship('MerchantModel',
                               backref=db.backref('items', lazy=True))

    def __init__(self, name, price, section):
        if is_none_or_empty(name):
            raise ValueError("Item Name {}".format(name))

        if is_integer(price):
            raise ValueError("Item Price {}".format(price))

        price = int(price)
        if price < 0:
            raise ValueError(
                "Item Price must be greater than 0, {}".format(price))

        if is_none_or_empty(section):
            raise ValueError("Item Section {}".format(section))

        self.name = name
        self.price = price
        self.section = section

    def __repr__(self):
        return "<ItemModel %r>" % self.name
