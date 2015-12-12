import unittest

from main import main

class SmallTestCases(unittest.TestCase):
    def test_small(self):
        self.assertEqual(main(start="1", steps=1), "11")
    def test_med(self):
        self.assertEqual(main(start="11", steps=1), "21")
        self.assertEqual(main(start="1211", steps=1), "111221")
        self.assertEqual(main(start="111221", steps=1), "312211")
    def test_large(self):
        pass
        


if __name__ == '__main__':
    unittest.main()