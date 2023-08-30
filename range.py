# Using range to create a list of odd numbers
odd_numbers = list(range(1, 21, 2))
print("List of odd numbers:", odd_numbers)

# Using range to iterate over indices and values of a list
fruits = ["apple", "banana", "orange", "grape"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Using range to create a countdown timer
import time
countdown = 10
for remaining in range(countdown, 0, -1):
    print(f"Countdown: {remaining}")
    time.sleep(1)
print("Blast off!")

# Using range with step to generate reversed sequence
reversed_sequence = list(range(10, 0, -1))
print("Reversed sequence:", reversed_sequence)

'''
En este ejemplo:

Hemos utilizado range para crear una lista de números impares del 1 al 20, con un paso de 2. Esto se logra mediante list(range(1, 21, 2)).

Hemos utilizado enumerate junto con range para iterar sobre los índices y valores de una lista.

Hemos utilizado range para crear un temporizador de cuenta regresiva, que muestra el conteo atrás desde 10 hasta 1, con una pausa de 1 segundo entre cada número.

Hemos utilizado range con un paso negativo para generar una secuencia inversa del 10 al 1.

Este ejemplo muestra algunas aplicaciones avanzadas del concepto de range en Python.
'''
