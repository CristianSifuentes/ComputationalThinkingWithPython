def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursive approach.
    
    Parameters:
        n (int): The index of the Fibonacci number to calculate.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dynamic(n):
    """
    Calculate the nth Fibonacci number using dynamic programming approach.
    
    Parameters:
        n (int): The index of the Fibonacci number to calculate.
        
    Returns:
        int: The nth Fibonacci number.
    """
    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i - 1] + fib_values[i - 2])
    return fib_values[n]

def fibonacci_tail_recursive(n, a=0, b=1):
    """
    Calculate the nth Fibonacci number using tail recursion.
    
    Parameters:
        n (int): The index of the Fibonacci number to calculate.
        a (int): The previous Fibonacci number.
        b (int): The current Fibonacci number.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return a
    else:
        return fibonacci_tail_recursive(n - 1, b, a + b)

# Test the Fibonacci functions
n = 10
print(f"The {n}th Fibonacci number using recursive approach is: {fibonacci_recursive(n)}")
print(f"The {n}th Fibonacci number using dynamic programming approach is: {fibonacci_dynamic(n)}")
print(f"The {n}th Fibonacci number using tail recursion is: {fibonacci_tail_recursive(n)}")


'''
En este ejemplo, hemos implementado tres enfoques para calcular el enésimo número de Fibonacci:

Recursión: fibonacci_recursive utiliza la recursión clásica para calcular los números de Fibonacci. Aunque es sencillo, puede ser ineficiente para números grandes debido a la repetición de cálculos.

Programación dinámica: fibonacci_dynamic utiliza programación dinámica para almacenar los valores previamente calculados y evitar cálculos redundantes. Esto mejora significativamente la eficiencia en comparación con la recursión simple.

Recursión de cola: fibonacci_tail_recursive implementa una forma de recursión de cola, donde los cálculos se realizan en la dirección descendente (desde n hasta 0) y los resultados se acumulan en los argumentos. Esto puede ser eficiente y evitar el desbordamiento de pila para números grandes.

Este ejemplo demuestra diferentes enfoques para calcular la serie de Fibonacci y resalta cómo la elección del enfoque puede influir en la eficiencia y la complejidad del algoritmo.
'''