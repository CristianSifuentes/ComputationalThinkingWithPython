'''
En este ejemplo, puedes ver cómo la función manipulate_with_function() 
toma otra función como argumento y utiliza esa función para realizar 
operaciones en el ámbito de la función. Además, la función inner_function() 
se define dentro de la función outer_function(), 
lo que permite el acceso a la variable outer_variable en su ámbito superior.

'''


# Función para multiplicar un número por 2
def multiply_by_2(x):
    return x * 2

# Función que toma otra función como parámetro y la usa para realizar operaciones
def manipulate_with_function(number, function):
    result = function(number)
    return result

# Variable global
global_variable = 10

# Llamada a la función manipulate_with_function y passando multiply_by_2 como argumento
result1 = manipulate_with_function(global_variable, multiply_by_2)
print("Resultado 1:", result1)  # Resultado: 20

# También puedes definir funciones dentro de funciones
def outer_function():
    outer_variable = 5
    
    def inner_function(x):
        return x + outer_variable
    
    return inner_function

# Crear una función interna usando outer_function
new_function = outer_function()

# Llamada a la función interna con un argumento
result2 = new_function(10)
print("Resultado 2:", result2)  # Resultado: 15