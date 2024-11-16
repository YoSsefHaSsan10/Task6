import unittest
from addcalculator import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, -4), -6)
        self.assertEqual(add(7, -3), 4)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
