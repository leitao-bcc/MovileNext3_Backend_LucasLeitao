from app import db
from app.models.base import BaseModel


class CustomerModel(db.Model, BaseModel):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    taxPayerIdentificationNumber = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(45), nullable=False)

    phone_id = db.Column(db.Integer, db.ForeignKey('phones.id'),
                         nullable=False)
    phone = db.relationship('PhoneModel')

    def __repr__(self):
        return "<CustomerModel %r>" % self.name
