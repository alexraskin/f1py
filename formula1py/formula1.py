import random
import requests

from typing import Optional
from dataclasses import dataclass


@dataclass
class ErgastResponse(object):
    """
    makes the request to the api
    url: [str] request url
    offset: [int] starting point of elements from API request
    limit: [int] number of items to return per request
    """

    url: str
    offset: Optional[int] = None
    limit: Optional[int] = None
    _json = None
    _xml = None
    _text = None

    def make_request(self, format_):
        self.url = f"{self.url}{format_}"
        if self.limit and self.offset:
            querystring = {"limit": self.limit, "offset": self.offset}
        else:
            querystring = None
        return requests.get(self.url, params=querystring)

    @property
    def xml(self):
        if self._xml is None:
            self._xml = self.make_request(".xml")
        return self._xml.text

    @property
    def json(self):
        if self._json is None:
            self._json = self.make_request(".json")
        return self._json.json()

    @property
    def text(self):
        if self._text is None:
            self._text = self.make_request(".xml")
        return self._text.text


@dataclass
class F1(object):
    secure: Optional[bool] = False
    offset: Optional[int] = None
    limit: Optional[int] = None

    __all__ = {
        "all_drivers": "drivers",
        "all_circuits": "circuits",
        "all_seasons": "seasons",
        "current_schedule": "current",
        "season_schedule": "{season}",
        "all_constructors": "constructors",
        "race_standings": "{season}/driverStandings",
        "constructor_standings": "{season}/constructorStandings",
        "driver_season": "{season}/drivers",
    }

    def __getattr__(self, attr):
        path = self.__all__.get(attr)
        if path is None:
            raise AttributeError

        def outer(path):
            def inner(**kwargs):
                url = self._build_url(path, **kwargs)
                return ErgastResponse(url)

            return inner

        return outer(self.__all__[attr])

    def random(self, **kwargs):
        applicable_actions = []
        for action in self.__all__.keys():
            applicable_actions.append(action)
        choice = getattr(self, random.choice(applicable_actions))
        return choice(**kwargs)

    def _build_url(self, path, **kwargs) -> str:
        url = "{protocol}://ergast.com/api/f1/{path}".format(
            protocol="https" if self.secure else "http", path=path.format(**kwargs)
        )
        return url


f1 = F1()
