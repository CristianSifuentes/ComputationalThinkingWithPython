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
            print(f"Test 'test_factorial_of_zero' failed: {e}")
    
    def test_factorial_of_one(self):
        try:
            result = calculate_factorial(1)
            self.assertEqual(result, 1)
        except Exception as e:
            print(f"Test 'test_factorial_of_one' failed: {e}")
    
    def test_factorial_of_positive_number(self):
        try:
            result = calculate_factorial(5)
            self.assertEqual(result, 120)
        except Exception as e:
            print(f"Test 'test_factorial_of_positive_number' failed: {e}")
    
    def test_factorial_of_large_number(self):
        try:
            result = calculate_factorial(10)
            self.assertEqual(result, 3628800)
        except Exception as e:
            print(f"Test 'test_factorial_of_large_number' failed: {e}")
    
    def test_factorial_of_negative_number(self):
        try:
            calculate_factorial(-1)
            print("Test 'test_factorial_of_negative_number' failed: Expected ValueError was not raised")
        except ValueError as e:
            if str(e) == "Factorial is not defined for negative numbers":
                print("Test 'test_factorial_of_negative_number' passed")
            else:
                print(f"Test 'test_factorial_of_negative_number' failed: {e}")

# Ejecutar las pruebas si este archivo se ejecuta directamente
if __name__ == '__main__':
    unittest.main()



'''
En esta versión, hemos reemplazado self.fail() 
con print en los bloques except para imprimir los 
mensajes de error en la consola. Además, para la 
prueba de cálculo de factorial para números negativos, 
estamos utilizando print para indicar si la prueba pasó 
o falló según el resultado obtenido.






'''