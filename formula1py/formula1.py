import json
import re
import urllib.parse
from dataclasses import dataclass
from typing import Optional

import requests
import requests_cache

requests_cache.install_cache(cache_name='f1_api_cache', backend='sqlite', expire_after=180)


class F1Exception(Exception):
    pass

@dataclass
class F1:
    """
    secure: [bool] http or https
    format_: [str] response format - defaults to json
    offset: [int] starting point of elements from API request
    limit: [int] number of items to return per request
    timeout: [int] set a timeout for the API
    """
    secure: Optional[bool] = False
    format_: Optional[str] = 'json' or 'xml' # grrr cannot use format so _
    limit: Optional[int] = 30
    offset: Optional[int] = 30
    timeout: Optional[int] = 15
        

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
            def inner():
                url = self._build_url(
                    path=path,
                    limit=self.limit,
                    offset=self.offset)
                return self._make_request(url=url)
            return inner 

        return outer(self.__all__[attr])

    def _build_url(self, path: str, **params: dict) -> str:
        url = "{protocol}://ergast.com/api/f1/{path}.{format_}?{params}".format(
            protocol="https" if self.secure else "http",
            path=path,
            format_='json' if self.format_ == 'json' else 'xml',
            params=urllib.parse.urlencode(params))
        return url

    def _make_request(self, url):
        try:
            response = requests.get(url=url, timeout=self.timeout)

        except requests.Timeout:
            raise F1Exception('Error: API Timeout')

        if response.status_code != 200:
            raise F1Exception(f'Returned NON-200:{response.status_code}')

        if self.format_ == 'json':
            return response.json()
        if self.format_ == 'xml':
            return response.text
        else:
            raise F1Exception('API Error')

f1 = F1(secure=True, format_='')

print(f1.all_drivers())