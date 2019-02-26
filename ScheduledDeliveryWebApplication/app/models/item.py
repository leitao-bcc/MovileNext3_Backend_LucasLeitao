from app import db
from app.models.base import BaseModel


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

    def __repr__(self):
        return "<ItemModel %r>" % self.name
