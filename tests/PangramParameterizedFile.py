import unittest
from sample.Pangram import *


class PangramParametrizedFile(unittest.TestCase):

    def test_from_file(self):
        file = open("data/pangram_tests_file")
        temporary_pangram = Pangram()
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                input_value, expected = (data[0], data[1].strip("\n"))
                self.assertEqual(temporary_pangram.is_pangram(input_value), bool(expected))
