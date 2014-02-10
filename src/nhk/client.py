import requests

from .area import AreaChoices
from .genre import GenreChoices
from .service import ServiceChoices


class ProgramGuide(object):
    def __init__(self, api_key=None, domain='api.nhk.or.jp', version='v1',
                 secure=False):
        """Returns NHK Program API client.

        :param api_key: Your API key.
        :type api_key: str
        :param domain: domain for API resource URL.
        :type domain: str
        :param version: API version.
        :type version: str
        :param secure: True if you connect with HTTPS instead of HTTP.
        :type secure: bool.
        """
        self.api_key = api_key
        scheme = 'https' if secure else 'http'
        self.url_base = '{scheme}://{netloc}/{version}/'.format(
            scheme=scheme, netloc=domain, version=version)

    def _to_ymd(self, date):
        return date.strftime('%Y-%m-%d')

    def _build_url(self, *args):
        url = self.url_base
        url += '/'.join(args)
        url += '.json'
        return url

    def pg_list(self, area, service, date):
        """Returns programs with the specified area, service and date.

        :param area: The area ID or name of the broadcasting area.
        :type area: str
        :param service: The service ID or name of the broadcasting
            station.
        :type service: str
        :param date: Specifies the broadcasting date.
        :type date: datetime.date
        """
        area = AreaChoices.detect(area).code
        service = ServiceChoices.detect(service).code
        url = self._build_url('pg', 'list', area, service, self._to_ymd(date))
        payload = {'key': self.api_key}
        response = requests.get(url, params=payload)

        return response.json()

    def pg_genre(self, area, service, genre, date):
        """Returns programs with the specified area, service, genre
        and date.

        :param area: The area ID or name of the broadcasting area.
        :type area: str
        :param service: The service ID or name of the broadcasting
            station.
        :type service: str
        :param genre: The genre ID or name of the genre code.
        :type genre: str
        :param date: Specifies the broadcasting date.
        :type date: datetime.date
        """
        area = AreaChoices.detect(area).code
        service = ServiceChoices.detect(service).code
        genre = GenreChoices.detect(genre).code
        url = self._build_url('pg', 'genre', area, service, genre,
                              self._to_ymd(date))
        payload = {'key': self.api_key}
        response = requests.get(url, params=payload)

        return response.json()

    def pg_info(self, area, service, program_id):
        """Returns the information of program with the specified
        program ID.

        :param area: The area ID or name of the broadcasting area.
        :type area: str
        :param service: The service ID or name of the broadcasting
            station.
        :type service: str
        :param program_id: The program ID.
        :type program_id: str
        """
        area = AreaChoices.detect(area).code
        service = ServiceChoices.detect(service).code
        url = self._build_url('pg', 'info', area, service, program_id)
        payload = {'key': self.api_key}
        response = requests.get(url, params=payload)

        return response.json()

    def pg_now(self, area, service):
        """Returns programs that is broadcasting now.

        :param area: The area ID or name of the broadcasting area.
        :type area: str
        :param service: The service ID or name of the broadcasting
            station.
        :type service: str
        """
        area = AreaChoices.detect(area).code
        service = ServiceChoices.detect(service).code
        url = self._build_url('pg', 'now', area, service)
        payload = {'key': self.api_key}
        response = requests.get(url, params=payload)

        return response.json()
