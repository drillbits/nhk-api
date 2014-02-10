import unittest

from testfixtures import compare
from testfixtures import ShouldRaise


class TestServiceChoicesDetect(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from nhk.service import ServiceChoices
        return ServiceChoices.detect(*args, **kwargs)

    def test_detect_by_service(self):
        from nhk.service import Service
        service = Service('666', 'spam')
        result = self._callFUT(service)

        compare(result.code, '666')
        compare(result.name, 'spam')

    def test_detect_by_code(self):
        result = self._callFUT('g1')

        compare(result.code, 'g1')
        compare(result.name, 'ＮＨＫ総合１')

    def test_detect_by_name(self):
        result = self._callFUT('ＮＨＫ総合１')

        compare(result.code, 'g1')
        compare(result.name, 'ＮＨＫ総合１')

    def test_detect_error(self):
        with ShouldRaise(KeyError('Service: ham not found')):
            self._callFUT('ham')
