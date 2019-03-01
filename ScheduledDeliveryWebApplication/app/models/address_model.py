from app import db
from app.models.base_model import BaseModel
from app.validators.cep_validator import is_valid_cep
from app.validators.coordinates_validator import is_valid_latitude, \
    is_valid_longitude
from app.validators.none_or_empty_validator import is_none_or_empty
from app.validators.string_format_validator import is_float


class AddressModel(db.Model, BaseModel):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    neighborhood = db.Column(db.String(45), nullable=False)
    street_name = db.Column(db.String(90), nullable=False)
    street_number = db.Column(db.String(10))
    postal_code = db.Column(db.String(10), nullable=False)
    complement = db.Column(db.String(45))
    latitude = db.Column(db.Float(precision="3,9"), nullable=False)
    longitude = db.Column(db.Float(precision="3,9"), nullable=False)

    def __init__(self, country, state, city, neighborhood, street_name,
                 street_number, postal_code, complement,
                 latitude, longitude):

        if is_none_or_empty(country):
            raise ValueError("Address Country {}".format(country))

        if is_none_or_empty(state):
            raise ValueError("Address State {}".format(state))

        if is_none_or_empty(city):
            raise ValueError("Address City {}".format(city))

        if is_none_or_empty(neighborhood):
            raise ValueError("Address Neighborhood {}".format(neighborhood))

        if is_none_or_empty(street_name):
            raise ValueError("Address StreetName {}".format(street_name))

        if not is_valid_cep(postal_code):
            raise ValueError("Address PostalCode {}".format(postal_code))

        if not is_float(latitude):
            raise ValueError("Address Latitude {}".format(latitude))

        latitude = float(latitude)
        if not is_valid_latitude(latitude):
            raise ValueError("Address Latitude {}".format(latitude))

        if not is_float(longitude):
            raise ValueError("Address Longitude {}".format(longitude))

        longitude = float(longitude)
        if not is_valid_longitude(longitude):
            raise ValueError("Address Longitude {}".format(longitude))

        self.country = country
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.complement = complement
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "<AddressModel %r>" % self.street_name

    def to_json(self):
        return {
            "country": self.country,
            "state": self.state,
            "city": self.city,
            "neighborhood": self.neighborhood,
            "streetName": self.street_name,
            "streetNumber": self.street_number,
            "postalCode": self.postal_code,
            "complement": self.complement,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
