from flask import Flask
from flask_restful import Api

from app.resources.auth_resource import AuthResource
from app.resources.catalog_resource import CatalogResource
from app.resources.merchant_resource import MerchantResource
from app.resources.order_resource import OrderResource

api = Api()

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    api.add_resource(CatalogResource, '/catalog')
    api.add_resource(MerchantResource, '/merchant/<string:merchant_id>')
    api.add_resource(AuthResource, '/auth/login')
    api.add_resource(OrderResource, '/order')

    return app
