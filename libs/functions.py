from gevent import Timeout
import gevent.monkey
gevent.monkey.patch_socket()

import urllib2
from BeautifulSoup import BeautifulSoup


class WebsiteNotFound(Exception):
    pass


class RequestWrapper(object):
    """
    A wrapper for making a request and storing response and making a call to a success/failure function.
    """
    result = None
    no_result = True

    def __init__(self, url):
        self.url = url

    def _get_url(self):
        if 'http://www.uci.infostradasports.com/' not in self.url:
            self.url = 'http://www.uci.infostradasports.com%s' % self.url
        return self.url

    def get_response(self):
        self.no_result = True
        try:
            response = urllib2.urlopen(self._get_url(), timeout=30)
            self.result = response.read()
            self.no_result = False
        except urllib2.URLError, e:
            print 'Timeout '
            pass

    def fetch_url(self):
        """
        Fetch the data from the url and call success or failure function.
        """
        while self.no_result:
            self.get_response()

        if self.is_all_results_or_no_results():
            return self.result
        self.get_response()

    def is_all_results_or_no_results(self):
        soup = BeautifulSoup(self.result)
        image = soup.find('img', {'src': '/images/buttons/AllPagesOn.gif'})
        if image:
            href = image.parent['href']
            self.url = 'http://www.uci.infostradasports.com/asp/lib/%s' % href
            return False
        return True

