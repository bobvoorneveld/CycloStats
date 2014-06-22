from django.test import TestCase

from .functions import RequestWrapper


class LibsTestCase(TestCase):
    url = 'http://www.uci.infostradasports.com/asp/lib/TheASP.asp?PageID=19004&SportID=102&CompetitionID=-1&EditionID=-1&SeasonID=-1&ClassID=1&GenderID=1&EventID=-1&EventPhaseID=0&Phase1ID=0&Phase2ID=0&Phase3ID=0&CompetitionCodeInv=1&Detail=1&Ranking=0&All=0&TaalCode=2&StyleID=0&Cache=8'
    short_url = '/asp/lib/TheASP.asp?PageID=19004&SportID=102&CompetitionID=-1&EditionID=-1&SeasonID=-1&ClassID=1&GenderID=1&EventID=-1&EventPhaseID=0&Phase1ID=0&Phase2ID=0&Phase3ID=0&CompetitionCodeInv=1&Detail=1&Ranking=0&All=0&TaalCode=2&StyleID=0&Cache=8'

    def test_url_not_changed(self):
        rw = RequestWrapper(self.url)
        url = rw._get_url()
        self.assertEqual(self.url, url)

    def short_url_extended(self):
        rw = RequestWrapper(self.short_url)
        url = rw._get_url()
        self.assertEqual(self.url, url)

    def test_params_added(self):
        rw = RequestWrapper(self.url, params={'testkey': 'testvalue'})
        url = rw._get_url()
        self.assertTrue('testkey=testvalue' in url)

    def test_params_updated(self):
        rw = RequestWrapper(self.url, params={'PageNr0': -2})
        url = rw._get_url()
        self.assertTrue('PageNr0=-2' in url)
        self.assertFalse('PageNr0=-1' in url)

    def test_retrieve_website(self):
        rw = RequestWrapper(self.url)
        rw.fetch_url()
        self.assertIsNotNone(rw.response)
