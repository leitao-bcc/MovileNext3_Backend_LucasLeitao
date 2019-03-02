from app import db
from app.models.base_model import BaseModel
from app.validators.phone_validator import is_valid_ddd, is_valid_phone_number
from app.validators.string_format_validator import is_integer


class PhoneModel(db.Model, BaseModel):
    __tablename__ = 'phones'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False)
    ddd = db.Column(db.Integer, nullable=False)

    def __init__(self, ddd, number):
        if not is_integer(ddd):
            raise ValueError("Phone DDD {}".format(ddd))

        ddd = int(ddd)
        if not is_valid_ddd(ddd):
            raise ValueError("Phone DDD {}".format(ddd))

        if not is_valid_phone_number(number):
            raise ValueError("Phone Number {}".format(number))

        self.ddd = ddd
        self.number = number

    def __repr__(self):
        return "<PhoneModel %r>" % self.number

    def to_json(self):
        return "{} {}".format(self.ddd, self.number)
