import unittest

from testfixtures import compare
from testfixtures import ShouldRaise


class TestGenreChoicesDetect(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from nhk.genre import GenreChoices
        return GenreChoices.detect(*args, **kwargs)

    def test_detect_by_area(self):
        from nhk.genre import Genre
        genre = Genre((0xD, 'spam'), (0x4, 'ham'))
        result = self._callFUT(genre)

        compare(result.code, '1304')
        compare(result.name, 'spam(ham)')

    def test_detect_by_code(self):
        result = self._callFUT('0700')

        compare(result.code, '0700')
        compare(result.name, 'アニメ／特撮(国内アニメ)')

    def test_detect_by_name(self):
        result = self._callFUT('アニメ／特撮(国内アニメ)')

        compare(result.code, '0700')
        compare(result.name, 'アニメ／特撮(国内アニメ)')

    def test_detect_error(self):
        with ShouldRaise(KeyError('Genre: ham not found')):
            self._callFUT('ham')
