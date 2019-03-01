from app import db
from app.models.base_model import BaseModel
from app.validators.none_or_empty_validator import is_none_or_empty


class CategoryModel(db.Model, BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def __init__(self, name):
        if is_none_or_empty(name):
            raise ValueError("Category Name {}".format(name))

        self.name = name

    def __repr__(self):
        return "<CategoryModel %r>" % self.name

    def to_json(self):
        return {
            "name": self.name
        }
