from app import db
from app.models.base import BaseModel


class CategoryModel(db.Model, BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return "<CategoryModel %r>" % self.name
