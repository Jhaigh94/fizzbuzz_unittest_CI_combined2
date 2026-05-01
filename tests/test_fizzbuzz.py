import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_no1_return_string(self):
        self.assertEqual(fizzbuzz(1),"1")
    
    def test_multiple_of3(self):
        self.assertEqual(fizzbuzz(3),"Fizz")

    def test_multiple_of5(self):
        self.assertEqual(fizzbuzz(5),"Buzz")

    def test_multiple_of3_and_5(self):
        self.assertEqual(fizzbuzz(15),"FizzBuzz")
if __name__ == "__main__":
    unittest.main()