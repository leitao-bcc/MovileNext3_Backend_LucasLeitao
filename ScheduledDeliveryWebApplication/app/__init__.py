from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.resources.auth_resource import AuthResource
from app.resources.catalog_resource import CatalogResource
from app.resources.merchant_resource import MerchantResource
from app.resources.order_resource import OrderResource
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

api = Api(app)

api.add_resource(CatalogResource, '/catalog')
api.add_resource(MerchantResource, '/merchant/<string:merchant_id>')
api.add_resource(AuthResource, '/auth/login')
api.add_resource(OrderResource, '/order/<string:order_id>')

from app.models import address_model, category_model, customer_model, \
    item_model, merchant_model, office_hour_model, order_model, order_item, \
    phone_model
