from urlparse import urlparse

import logging
import requests


logger = logging.getLogger('solr_detective.app')


class BaseDao(object):

    def __init__(self):
        pass


class HttpBaseDao(BaseDao):

    PROXIES = None

    def parse_url_data(self, url):
        result = urlparse(url)
        return {
            'error_url': url,
            'error_host': result.netloc,
            'error_url_path': result.path,
            'error_url_query_string': result.query
        }

    def get_data(self, url, **kwargs):
        try:
            if self.PROXIES:
                return requests.get(url, proxies=self.PROXIES, **kwargs)
            else:
                return requests.get(url, **kwargs)
        except requests.exceptions.ConnectTimeout as e:
            logger.error('HttpBaseDao Connection timeout',
                         extra=self.parse_url_data(url))
        except requests.exceptions.ReadTimeout as e:
            logger.error('HttpBaseDao Read timeout',
                         extra=self.parse_url_data(url))
        except requests.exceptions.ConnectionError as e:
            logger.error('HttpBaseDao Connection error',
                         extra=self.parse_url_data(url))

    def post_data(self, url, **kwargs):
        try:
            if self.PROXIES:
                return requests.post(url, proxies=self.PROXIES, **kwargs)
            else:
                return requests.post(url, **kwargs)
        except requests.exceptions.ConnectTimeout as e:
            logger.error('HttpBaseDao Connection timeout',
                         extra=self.parse_url_data(url))
        except requests.exceptions.ReadTimeout as e:
            logger.error('HttpBaseDao Read timeout',
                         extra=self.parse_url_data(url))
        except requests.exceptions.ConnectionError as e:
            logger.error('HttpBaseDao Connection error',
                         extra=self.parse_url_data(url))
