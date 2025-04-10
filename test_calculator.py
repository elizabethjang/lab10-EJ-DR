#https://github.com/elizabethjang/lab10-EJ-DR.git
#Partner 1: Elizabeth Jang
#Partner 2: Derek Rosales
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 5), 4)
        self.assertEqual(calculator.add(0.23, 0.25), 0.48)
    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(-5, 5), -10)
        self.assertEqual(calculator.subtract(0.25, 0.1), 0.15)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        pass
    def test_divide(self): # 3 assertions
        pass
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)
    def test_logarithm(self): # 3 assertions
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 20)
            calculator.logarithm(10, -5)
        self.assertEqual(calculator.logarithm(100, 10), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(5, 1)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()