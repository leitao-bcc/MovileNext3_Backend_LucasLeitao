from app import db
from app.models.base import BaseModel


class PhoneModel(db.Model, BaseModel):
    __tablename__ = 'phones'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False)
    ddd = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<PhoneModel %r>" % self.number
