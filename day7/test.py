import unittest

from main import main

class SmallTestCase(unittest.TestCase):
    test_data = ['123 -> x',
                 '456 -> y',
                 'x AND y -> d',
                 'x OR y -> e',
                 'x LSHIFT 2 -> f',
                 'y RSHIFT 2 -> g',
                 'NOT x -> h',
                 'NOT y -> i']

    def test_one(self):
        # self.assertEqual(main(["toggle 461,550 through 564,900"]), )
        self.assertEqual(main(self.test_data, 'd'), 72)

if __name__ == '__main__':
    unittest.main()
