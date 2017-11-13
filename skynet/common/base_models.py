from skynet.common.base_daos import BaseDao


class BaseModel(object):

    DEFAULT_DAO = BaseDao

    def __init__(self, dao=None):
        if dao is None:
            dao = self.DEFAULT_DAO()
        self.dao = dao

    def populate(self, data):
        for k, v in data.iteritems():
            k_translated = self.translate(k)
            if k_translated and hasattr(self, k_translated):
                setattr(self, k_translated, v)

    def translate(self, key):
        return {}.get(key, key)
