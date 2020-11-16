import unittest
from sample.Pangram import *


class PangramParametrizedFile(unittest.TestCase):

    def test_from_file(self):
        file = open("../data/pangram_tests_file")
        temporaryPangram = Pangram()
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                input, expected = str(data[0], data[1].strip("\n"))
                self.assertEqual(temporaryPangram.is_pangram(input), bool(expected))
