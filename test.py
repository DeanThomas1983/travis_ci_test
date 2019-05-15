import unittest
from main import add, mul


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertTrue(4 == add(2, 2))

    def test_mul(self):
        self.assertEqual(4, mul(2, 2))


if __name__ == '__main__':
    unittest.main()
