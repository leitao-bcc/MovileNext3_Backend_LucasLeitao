from app import db
from app.models.base_model import BaseModel
from app.validators.none_or_empty_validator import is_none_or_empty
from app.validators.rating_validator import is_valid_rating
from app.validators.string_format_validator import is_float

merchant_phones = db.Table('merchant_phones',
                           db.Column('merchant_id',
                                     db.Integer,
                                     db.ForeignKey('merchants.id'),
                                     primary_key=True),
                           db.Column('phone_id',
                                     db.Integer,
                                     db.ForeignKey('phones.id'),
                                     primary_key=True)
                           )


class MerchantModel(db.Model, BaseModel):
    __tablename__ = 'merchants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float(precision="1,2"))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),
                            nullable=False)
    category = db.relationship('CategoryModel')

    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'),
                           nullable=False)
    address = db.relationship('AddressModel')

    phones = db.relationship('PhoneModel',
                             secondary=merchant_phones,
                             lazy='subquery')

    def __init__(self, name, description, rating):
        if is_none_or_empty(name):
            raise ValueError("Merchant Name {}".format(name))

        if is_none_or_empty(description):
            raise ValueError("Merchant Description {}".format(description))

        if not is_float(rating):
            raise ValueError("Merchant Rating {}".format(rating))

        rating = float(rating)
        if not is_valid_rating(rating):
            raise ValueError("Merchant Rating {}".format(rating))

        self.name = name
        self.description = description
        self.rating = rating

    def __repr__(self):
        return "<MerchantModel %r>" % self.name
