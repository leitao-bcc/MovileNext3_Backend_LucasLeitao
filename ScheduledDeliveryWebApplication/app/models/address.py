from app import db
from app.models.base import BaseModel


class AddressModel(db.Model, BaseModel):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    neighborhood = db.Column(db.String(45), nullable=False)
    streetName = db.Column(db.String(90), nullable=False)
    streetNumber = db.Column(db.String(10))
    postalCode = db.Column(db.String(10), nullable=False)
    complement = db.Column(db.String(45))
    latitude = db.Column(db.Float(precision="3,9"), nullable=False)
    longitude = db.Column(db.Float(precision="3,9"), nullable=False)

    def __repr__(self):
        return "<AddressModel %r>" % self.streetName
