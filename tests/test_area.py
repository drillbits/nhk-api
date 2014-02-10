import unittest

from testfixtures import compare
from testfixtures import ShouldRaise


class TestAreaChoicesDetect(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from nhk.area import AreaChoices
        return AreaChoices.detect(*args, **kwargs)

    def test_detect_by_area(self):
        from nhk.area import Area
        area = Area('666', 'spam')
        result = self._callFUT(area)

        compare(result.code, '666')
        compare(result.name, 'spam')

    def test_detect_by_code(self):
        result = self._callFUT('130')

        compare(result.code, '130')
        compare(result.name, '東京')

    def test_detect_by_name(self):
        result = self._callFUT('東京')

        compare(result.code, '130')
        compare(result.name, '東京')

    def test_detect_error(self):
        with ShouldRaise(KeyError('Area: ham not found')):
            self._callFUT('ham')
