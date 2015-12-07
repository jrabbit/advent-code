import unittest

from main import main

class SmallTestCase(unittest.TestCase):
    def test_one(self):
        # self.assertEqual(main(["toggle 461,550 through 564,900"]), )
        self.assertEqual(main(["toggle 0,0 through 999,0"]), 1000)

if __name__ == '__main__':
    unittest.main()