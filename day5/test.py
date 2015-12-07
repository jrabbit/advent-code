import unittest

from main import is_nice, is_nice2

class NiceTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"))
        self.assertTrue(is_nice("aaa"))
    def test_negatives(self):
        self.assertFalse(is_nice("jchzalrnumimnmhp"))
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))

class NiceTwoPointOh(unittest.TestCase):
    def test_nice(self):
        self.assertTrue(is_nice2("qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_nice2("xxyxx"))
    def test_naughty(self):
        self.assertFalse(is_nice2("uurcxstgmygtbstg"))
        self.assertFalse(is_nice2("ieodomkazucvgmuy"))


if __name__ == '__main__':
    unittest.main()