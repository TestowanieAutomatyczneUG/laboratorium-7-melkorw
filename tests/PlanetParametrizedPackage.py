import unittest
from sample.Planet import *
from parameterized import parameterized, parameterized_class

class PlanetParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Planet()

    @parameterized.expand([
        (1000000, 'Ziemia', 1000000),
        (23333311, 'Merkury', 3.07),
        (433323, 'Wenus', 0.02),
        (129999990, 'Mars', 2.19),
    ])
    def test_count_age_parameterized(self, earth_years, planet, expected):
        self.assertEqual(self.tmp.count_age(earth_years, planet), expected)


if __name__ == '__main__':
    unittest.main()
