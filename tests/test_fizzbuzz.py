import unittest
from fizzbuzz import fizzbuzz, fizzbuzz_list

class TestFizzBuzz(unittest.TestCase):
    def test_no1_return_string(self):
        self.assertEqual(fizzbuzz(1),"1")
    
    def test_multiple_of3(self):
        self.assertEqual(fizzbuzz(3),"Fizz")

    def test_multiple_of5(self):
        self.assertEqual(fizzbuzz(5),"Buzz")

    def test_multiple_of3_and_5(self):
        self.assertEqual(fizzbuzz(15),"FizzBuzz")

    def test_fizzbuzz_list_returns_100_items(self):
        result = fizzbuzz_list(100)
        self.assertEqual(len(result),100)
        self.assertEqual(result[0],"1") #1
        self.assertEqual(result[2],"Fizz") # for values of 3
        self.assertEqual(result[4],"Buzz") # for values of 5
        self.assertEqual(result[14],"FizzBuzz") # For values of 15 
        self.assertEqual(result[99],"Buzz") 
if __name__ == "__main__":
    unittest.main()