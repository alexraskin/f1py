"""
Python package that wraps Ergast F1 API
usage: from formula1 import F1
	f1 = F1()
	f1 = F1(secure=False, limit=30, offset=30)
	f1.driver_season(season=2020).xml
	f1.all_circuits().json
	f1.current_schedule().url
"""
from .formula1 import F1

__version__ = "0.6.0"
__license__ = "MIT"
