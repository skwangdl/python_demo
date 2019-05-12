from awesome_python3_webapp.www.static import ModelMetaclass
import logging

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

def getValueOrDefault(self, key):
    value = getattr(self, key, None)
    if value is None:
        field = self.__mappings__[key]
        if field.default is not None:
            value = field.default() if callable(field.default) else field.default
            logging.debug('using default value for %s: %s' % (key, str(value)))
            setattr(self, key, value)
    return value
