from app import db
from app.models.base import BaseModel


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

    def __repr__(self):
        return "<OrderItemModel %r>" % self.id
