import unittest
from formula1py.formula1 import F1


class Formula1Tests(unittest.TestCase):
    def setUp(self):
        self.f1 = F1()

    def test_url(self):
        url = self.f1.race_standings(season=2020).url
        self.assertEqual("http://ergast.com/api/f1/2020/driverStandings", url)

    def test_url_secure(self):
        secure_f1 = F1(secure=True)
        url = secure_f1.constructor_standings(season=2012).url
        self.assertEqual("https://ergast.com/api/f1/2012/constructorStandings", url)


if __name__ == "__main__":
    unittest.main()
