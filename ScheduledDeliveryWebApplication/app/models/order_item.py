from app import db
from app.models.base_model import BaseModel
from app.validators.none_or_empty_validator import is_none_or_empty
from app.validators.string_format_validator import is_integer


class OrderItemModel(db.Model, BaseModel):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer)
    quantity = db.Column(db.Integer, nullable=False)
    addition = db.Column(db.String(45))
    observations = db.Column(db.Text)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'),
                         nullable=False)
    order = db.relationship('OrderModel',
                            backref=db.backref('items', lazy=True))

    def __init__(self, name, price, discount, quantity, addition, observations):
        if is_none_or_empty(name):
            raise ValueError("OrderItem Name {}".format(name))

        if not is_integer(price):
            raise ValueError("OrderItem Price {}".format(price))

        price = int(price)
        if price < 0:
            raise ValueError("OrderItem Price must be greater than 0, {}".format(price))

        if not is_none_or_empty(discount):
            if not is_integer(discount):
                raise ValueError("OrderItem Discount {}".format(discount))

            discount = int(discount)
            if discount > price:
                raise ValueError("OrderItem Price must be greater than Discount, {} - {}".format(price, discount))

        if not is_integer(quantity):
            raise ValueError("OrderItem Price {}".format(price))

        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("OrderItem Quantity must be greater than 0, {}".format(quantity))

        self.name = name
        self.price = price
        self.discount = discount
        self.quantity = quantity
        self.addition = addition
        self.observations = observations

    def __repr__(self):
        return "<OrderItemModel %r>" % self.id

    def to_json(self):
        return {
            "name": self.name,
            "price": self.price,
            "discount": self.discount,
            "quantity": self.quantity,
            "addition": self.addition,
            "observations": self.observations
        }


