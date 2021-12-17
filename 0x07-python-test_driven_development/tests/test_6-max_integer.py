import unittest
max_integer = __import__('6-max_integer').max_integer

""" a unit test module """


class TestMax(unittest.TestCase):
    """ TestMax function that checks for correct output """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 7, 2, 4]), 7)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, -2]), 4)

    def test_max_integer(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)


if __name__ == '__main__':
    unittest.main()
