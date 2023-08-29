# Función que toma una función como argumento y aplica la función a una lista
def apply_function(func, values):
    return [func(x) for x in values]

# Función que devuelve una función lambda con una expresión
def create_lambda(expression):
    return lambda x: eval(expression)

# Función que suma dos números y devuelve la función suma
def create_add_function():
    def add(x, y):
        return x + y
    return add

# Definición de una función normal
def square(x):
    return x ** 2

# Lista de valores
numbers = [1, 2, 3, 4, 5]

# Pasar la función square como argumento y aplicarla a la lista
squared_values = apply_function(square, numbers)
print("Squared values:", squared_values)

# Crear una función lambda y aplicarla a la lista
lambda_expression = "x * 3"
lambda_function = create_lambda(lambda_expression)
lambda_values = apply_function(lambda_function, numbers)
print(f"Values using lambda ({lambda_expression}):", lambda_values)

# Crear una función que suma y utilizarla para sumar elementos de la lista
add_function = create_add_function()
sum_result = add_function(numbers[0], numbers[1])
print("Sum result:", sum_result)

'''
En este ejemplo, hemos demostrado:

El uso de una función que toma una función como argumento (apply_function) para aplicar funciones a una lista de valores.
La creación de una función lambda utilizando create_lambda y luego aplicándola a una lista.
La definición de una función anidada (create_add_function) que devuelve una función add.
Cómo se pueden usar funciones en expresiones, como en sum_result.
Este ejemplo abarca varios conceptos avanzados relacionados con el uso flexible y expresivo de funciones en Python.
'''