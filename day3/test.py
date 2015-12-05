import unittest

from main import part2

class RoboSanta(unittest.TestCase):
    def test_small(self):
        self.assertEqual(part2("^v"), 3)
    def test_med(self):
        self.assertEqual(part2("^>v<"), 3)
    def test_large(self):
        self.assertEqual(part2("^v^v^v^v^v"), 11)


if __name__ == '__main__':
    unittest.main()