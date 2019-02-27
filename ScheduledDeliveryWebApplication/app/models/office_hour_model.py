from app import db
from app.models.base_model import BaseModel
from app.validators.datetime_validator import is_valid_week_day, \
    is_valid_time_format


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

    def __init__(self, week_day, start_time, end_time):
        if not is_valid_week_day(week_day):
            raise ValueError("OfficeHour WeekDay {}".format(week_day))

        if not is_valid_time_format(start_time):
            raise ValueError("OfficeHour StartTime {}".format(start_time))

        if not is_valid_time_format(end_time):
            raise ValueError("OfficeHour EndTime {}".format(end_time))

        if start_time > end_time:
            raise ValueError(
                "OfficeHour EndTime must be greater than StartTime {} - {}".format(
                    start_time, end_time))

        self.week_day = week_day
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "<OfficeHourModel %r>" % self.merchant.name
