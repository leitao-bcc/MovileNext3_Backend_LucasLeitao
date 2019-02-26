from app import db
from app.models.base import BaseModel


class OfficeHourModel(db.Model, BaseModel):
    __tablename__ = 'office_hours'

    id = db.Column(db.Integer, primary_key=True)
    week_day = db.Column(db.String(3), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'),
                            nullable=False)
    merchant = db.relationship('MerchantModel',
                               backref=db.backref('office_hours', lazy=True))

    def __repr__(self):
        return "<OfficeHourModel %r>" % self.merchant.name
