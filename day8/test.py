import unittest

from main import main, part2


class TestCase(unittest.TestCase):
    test_list = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
    def test_main(self):
        self.assertEqual(main(self.test_list), 12)
    def test_part2(self):
        self.assertEqual(part2(self.test_list), 19)

if __name__ == '__main__':
    unittest.main()
