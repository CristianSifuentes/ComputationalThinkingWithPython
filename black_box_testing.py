import unittest

# Clase para realizar operaciones matemáticas
class MathOperations:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

# Pruebas utilizando el módulo unittest
class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()
    
    def test_addition(self):
        result = self.math_ops.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_subtraction(self):
        result = self.math_ops.subtract(10, 4)
        self.assertEqual(result, 6)
    
    def test_multiplication(self):
        result = self.math_ops.multiply(2, 6)
        self.assertEqual(result, 12)
    
    def test_division(self):
        result = self.math_ops.divide(15, 3)
        self.assertEqual(result, 5)
        
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.math_ops.divide(10, 0)

# Ejecutar las pruebas si este archivo se ejecuta directamente
if __name__ == '__main__':
    unittest.main()

    # Solicitar entradas manuales para realizar pruebas adicionales
    math_ops = MathOperations()

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        print("Addition:", math_ops.add(a, b))
        print("Subtraction:", math_ops.subtract(a, b))
        print("Multiplication:", math_ops.multiply(a, b))
        print("Division:", math_ops.divide(a, b))

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)
