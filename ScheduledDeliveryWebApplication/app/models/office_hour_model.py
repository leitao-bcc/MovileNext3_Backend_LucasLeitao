from datetime import datetime

from app import db
from app.models.base_model import BaseModel
from app.validators.datetime_validator import is_valid_week_day, \
    is_valid_time_format, TIME_FORMAT


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
        self.start_time = datetime.strptime(start_time, TIME_FORMAT)
        self.end_time = datetime.strptime(end_time, TIME_FORMAT)

    def __repr__(self):
        return "<OfficeHourModel %r>" % self.merchant.name

    def to_json(self):
        return {
            "weekDay": self.week_day,
            "startTime": self.start_time.strftime(TIME_FORMAT),
            "endTime": self.end_time.strftime(TIME_FORMAT)
        }

