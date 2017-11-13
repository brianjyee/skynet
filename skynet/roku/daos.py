"""SQLAlchemy model definitions."""

from skynet.common.base_daos import HttpBaseDao


class RokuDao(HttpBaseDao):
    """Defines the breakfast table."""

    def __init__(self):
        super(RokuDao, self).__init__()
