from app import db
from app.models.base import BaseModel

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

    def __repr__(self):
        return "<MerchantModel %r>" % self.name
