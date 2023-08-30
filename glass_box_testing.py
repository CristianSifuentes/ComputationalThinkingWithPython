import unittest

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Pruebas de caja de cristal utilizando unittest
class TestCalculateFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        try:
            result = calculate_factorial(0)
            self.assertEqual(result, 1)
        except Exception as e:
            self.fail(f"Test failed unexpectedly: {e}")
    
    def test_factorial_of_one(self):
        try:
            result = calculate_factorial(1)
            self.assertEqual(result, 1)
        except Exception as e:
            self.fail(f"Test failed unexpectedly: {e}")
    
    def test_factorial_of_positive_number(self):
        try:
            result = calculate_factorial(5)
            self.assertEqual(result, 120)
        except Exception as e:
            self.fail(f"Test failed unexpectedly: {e}")
    
    def test_factorial_of_large_number(self):
        try:
            result = calculate_factorial(10)
            self.assertEqual(result, 3628800)
        except Exception as e:
            self.fail(f"Test failed unexpectedly: {e}")
    
    def test_factorial_of_negative_number(self):
        try:
            calculate_factorial(-423423)
            self.fail("Expected ValueError was not raised")
        except ValueError as e:
            self.assertEqual(str(e), "Factorial is not defined for negative numbers")

# Ejecutar las pruebas si este archivo se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
