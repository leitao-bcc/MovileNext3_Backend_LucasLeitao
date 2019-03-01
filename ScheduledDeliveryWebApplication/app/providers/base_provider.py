class BaseProvider:

    def get_catalog(self, **kwargs):
        raise NotImplementedError()

    def get_merchant(self, merchant_id):
        raise NotImplementedError()

    def login(self, username, password):
        raise NotImplementedError()

    def post_order(self, **kwargs):
        raise NotImplementedError()
