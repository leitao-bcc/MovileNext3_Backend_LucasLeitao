class BaseTransform:

    def transform_catalog(self, data):
        raise NotImplementedError()

    def transform_merchant(self, data):
        raise NotImplementedError()

    def transform_login(self, data):
        raise NotImplementedError()
