import unittest

from main import validator, main

class ValidatorTestCase(unittest.TestCase):
    def test_string1(self):
        self.assertFalse(validator("hijklmmn"))
    def test_string2(self):
        self.assertFalse(validator("abbceffg"))
    def test_string3(self):
        self.assertFalse(validator("abbcegjk"))

class IteratorTestCase(unittest.TestCase):
    def test_input1(self):
        self.assertEqual(main("abcdefgh"), "abcdffaa")
    def test_input2(self):
        self.assertEqual(main("ghijklmn"), "ghjaabcc")

if __name__ == '__main__':
    unittest.main()
