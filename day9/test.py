import unittest
from main import main, get_locs


class SmallTestCase(unittest.TestCase):
    test_data = ['London to Dublin = 464',
                 'London to Belfast = 518',
                 'Dublin to Belfast = 141']

    def test_get_locs(self):
        self.assertEqual(
            get_locs(self.test_data), set(['Dublin', 'London', 'Belfast']))

    def test_one(self):
        self.assertEqual(main(self.test_data), 605)

if __name__ == '__main__':
    unittest.main()
