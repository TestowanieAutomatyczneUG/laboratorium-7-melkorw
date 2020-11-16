import unittest
from sample.Planet import *
from parameterized import parameterized, parameterized_class

class PlanetParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Planet()

    @parameterized.expand([
        (1000000, 'Ziemia', 0.03),
        (23333311, 'Merkury', 3.07),
        (433323, 'Wenus', 0.02),
        (129999990, 'Mars', 2.19),
    ])
    def test_count_age_parameterized(self, earth_years, planet, expected):
        self.assertEqual(self.tmp.count_age(earth_years, planet), expected)


@parameterized_class(('earth_years', 'planet', 'expected'), [
    (3299559992, 'Jowisz', 8.81),
    (49922292, 'Saturn', 0.05),
    (378843333, 'Uran', 0.14),
    (332211111, 'Neptun', 0.06),
])
class PlanetParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Planet()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.count_age(self.earth_years, self.planet), self.expected)


if __name__ == '__main__':
    unittest.main()
