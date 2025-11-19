import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
     def test_add(self): # 3 assertions
         self.assertEqual(add(2, 3), 5)
         self.assertEqual(add(-1, 4), 3)

     def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 4), -4)

    ######## Partner 1
     def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(-8, 3), -24)
        self.assertEqual(mul(-5, -4), 20)


     def test_divide(self): # 3 assertions
        self.assertEqual(div(20, 4), 5)
        self.assertEqual(div(5, -5), -1)
        self.assertNotEqual((7, 3), 6)

     ######## Partner 2
     def test_divide_by_zero(self): # 1 assertion
         error_raised = False
         try:
             div(0, 5)
         except ZeroDivisionError:
             error_raised = True
         self.assertTrue(error_raised)

     def test_logarithm(self): # 3 assertions
         self.assertAlmostEqual(log(10, 100), 2.0)
         self.assertAlmostEqual(log(2, 8), 3.0)

     def test_log_invalid_base(self): # 1 assertion
         self.assertAlmostEqual(log(10, 100), 2.0)
         self.assertAlmostEqual(log(2, 8), 3.0)

    
    ######## Partner 1
     def test_log_invalid_argument(self): # 1 assertion
         # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
          # log(0) is undefined
          with self.assertRaises(ValueError):
              log(0, 5)
    #     fill in code

     def test_hypotenuse(self): # 3 assertions
        self.assertEqual((3, 4), 5)
        self.assertEqual((5, 7), 12)
        self.assertNotEqual((1, 8), 3)


     def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
          with self.assertRaises(ValueError):
              square_root(-2)
    #     # Test basic function
    #     fill in code
          self.assertEqual(4, 2)
          self.assertEqual(64, 8)
          self.assertNotEqual(72, 9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()