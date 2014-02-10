import os
import unittest
from datetime import date, timedelta

from testfixtures import compare
from testfixtures import ShouldRaise


class TestProgramListAPI(unittest.TestCase):
    def _getClient(self):
        if not getattr(self, '_client', None):
            api_key = os.environ.get('NHK_API_KEY', None)
            from nhk import ProgramGuide
            self._client = ProgramGuide(api_key=api_key)
        return self._client

    def _callFUT(self, *args, **kwargs):
        client = self._getClient()
        return client.pg_list(*args, **kwargs)

    def test_today(self):
        today = date.today()
        result = self._callFUT('130', 'g1', today)

        self.assertNotEqual(result.get('list'), None)

    def test_tomorrow(self):
        tomorrow = date.today() + timedelta(days=1)
        result = self._callFUT('130', 'g1', tomorrow)

        self.assertNotEqual(result.get('list'), None)

    def test_day_after_tomorrow(self):
        day_after_tomorrow = date.today() + timedelta(days=2)
        result = self._callFUT('130', 'g1', day_after_tomorrow)

        compare(result,
                {'error': {'message': 'Invalid parameters', 'code': 1}})

    def test_invalid_area(self):
        today = date.today()
        with ShouldRaise(KeyError):
            self._callFUT('spam', 'g1', today)

    def test_invalid_service(self):
        today = date.today()
        with ShouldRaise(KeyError):
            self._callFUT('130', 'spam', today)


class TestProgramGenreAPI(unittest.TestCase):
    def _getClient(self):
        if not getattr(self, '_client', None):
            api_key = os.environ.get('NHK_API_KEY', None)
            from nhk import ProgramGuide
            self._client = ProgramGuide(api_key=api_key)
        return self._client

    def _callFUT(self, *args, **kwargs):
        client = self._getClient()
        return client.pg_genre(*args, **kwargs)

    def test_today(self):
        today = date.today()
        result = self._callFUT('130', 'g1', '0700', today)

        self.assertNotEqual(result.get('list'), None)

    def test_tomorrow(self):
        tomorrow = date.today() + timedelta(days=1)
        result = self._callFUT('130', 'g1', '0700', tomorrow)

        self.assertNotEqual(result.get('list'), None)

    def test_day_after_tomorrow(self):
        day_after_tomorrow = date.today() + timedelta(days=2)
        result = self._callFUT('130', 'g1', '0700', day_after_tomorrow)

        compare(result,
                {'error': {'message': 'Invalid parameters', 'code': 1}})

    def test_invalid_area(self):
        today = date.today()
        with ShouldRaise(KeyError):
            self._callFUT('spam', 'g1', '0700', today)

    def test_invalid_service(self):
        today = date.today()
        with ShouldRaise(KeyError):
            self._callFUT('130', 'spam', '0700', today)

    def test_invalid_genre(self):
        today = date.today()
        with ShouldRaise(KeyError):
            self._callFUT('130', 'g1', 'spam', today)


class TestProgramInformationAPI(unittest.TestCase):
    def _getClient(self):
        if not getattr(self, '_client', None):
            api_key = os.environ.get('NHK_API_KEY', None)
            from nhk import ProgramGuide
            self._client = ProgramGuide(api_key=api_key)
        return self._client

    def _callFUT(self, *args, **kwargs):
        client = self._getClient()
        return client.pg_info(*args, **kwargs)

    def _get_program_id(self, area, service, date_):
        program_list = self._getClient().pg_list(area, service, date_)
        return program_list['list']['g1'][0]['id']

    def test_it(self):
        today = date.today()
        program_id = self._get_program_id('130', 'g1', today)
        result = self._callFUT('130', 'g1', program_id)

        self.assertNotEqual(result.get('list'), None)

    def test_invalid_area(self):
        today = date.today()
        program_id = self._get_program_id('130', 'g1', today)
        with ShouldRaise(KeyError):
            self._callFUT('spam', 'g1', program_id)

    def test_invalid_service(self):
        today = date.today()
        program_id = self._get_program_id('130', 'g1', today)
        with ShouldRaise(KeyError):
            self._callFUT('130', 'spam', program_id)

    def test_invalid_program_id(self):
        result = self._callFUT('130', 'g1', 'spam')

        compare(
            result, {
                'fault': {
                    'faultstring': 'Not Found',
                    'detail': {
                        'errorcode': 'CLASSIFICATION_FAILURE'
                    }
                }
            })


class TestProgramNowAPI(unittest.TestCase):
    def _getClient(self):
        if not getattr(self, '_client', None):
            api_key = os.environ.get('NHK_API_KEY', None)
            from nhk import ProgramGuide
            self._client = ProgramGuide(api_key=api_key)
        return self._client

    def _callFUT(self, *args, **kwargs):
        client = self._getClient()
        return client.pg_now(*args, **kwargs)

    def test_it(self):
        result = self._callFUT('130', 'g1')

        self.assertNotEqual(result.get('nowonair_list'), None)

    def test_invalid_area(self):
        with ShouldRaise(KeyError):
            self._callFUT('spam', 'g1')

    def test_invalid_service(self):
        with ShouldRaise(KeyError):
            self._callFUT('130', 'spam')
