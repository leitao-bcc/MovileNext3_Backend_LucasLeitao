from app import db
from app.models.base import BaseModel
from app.validators.none_or_empty_validator import is_none_or_empty
from app.validators.identification_number_validator import is_valid_cpf, is_valid_cnpj
from app.validators.email_validator import is_valid_email


class CustomerModel(db.Model, BaseModel):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    taxPayerIdentificationNumber = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(45), nullable=False)

    phone_id = db.Column(db.Integer, db.ForeignKey('phones.id'),
                         nullable=False)
    phone = db.relationship('PhoneModel')

    def __init__(self, name, tax_payer_identification_number, email):
        if is_none_or_empty(name):
            raise ValueError("Customer Name {}".format(name))

        if not is_valid_cpf(tax_payer_identification_number) and not is_valid_cnpj(tax_payer_identification_number):
            raise ValueError("Customer TaxPayerIdentificationNumber {}".format(tax_payer_identification_number))

        if not is_valid_email(email):
            raise ValueError("Customer Email {}".format(email))

        self.name = name
        self.taxPayerIdentificationNumber = tax_payer_identification_number
        self.email = email

    def __repr__(self):
        return "<CustomerModel %r>" % self.name
