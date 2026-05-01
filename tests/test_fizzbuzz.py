import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_no1_return_string(self):
        self.assertEqual(fizzbuzz(1),"1")

if __name__ == "__main__":
    unittest.main()