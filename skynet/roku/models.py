"""SQLAlchemy model definitions."""

from skynet.common.base_models import BaseModel
from skynet.roku.daos import RokuDao


class RokuModel(BaseModel):
    """Defines the breakfast table."""
    base_url = 'http://192.168.1.8:8060'
    action = ''
    command = ''

    def __init__(self):
        super(RokuModel, self).__init__()

    def load(self, action, command):
        self.action = action
        self.command = command

    def send_command(self):
        url = '{}/{}/{}'.format(
            self.base_url,
            self.action,
            self.command
        )
        dao = RokuDao()
        dao.post_data(url)
        return {
            'action': self.action,
            'command': self.command,
            'url': url,
            'status': 'success'
        }

    def get_launch_app_id(self, channel):
        channels = {
            "abc": 73376,
            "amazon": 13,
            "amazon prime": 13,
            "amazon video": 13,
            "hbo": 8378,
            "hbo go": 8378,
            "hulu": 2285,
            "netflix": 12,
            "youtube": 837
        }
        return channels[channel]
