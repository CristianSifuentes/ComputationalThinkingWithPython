# Variable global
global_variable = "Soy una variable global"

def function_with_local_variable():
    # Variable local dentro de la función
    local_variable = "Soy una variable local"
    print(local_variable)

def function_with_global_variable():
    # Usar la variable global dentro de la función
    print(global_variable)

def function_with_parameter(parameter):
    # Usar el parámetro de la función
    print("El valor del parámetro es:", parameter)

# Llamada a las funciones
print("Ejemplo de ámbito de variables:")
function_with_local_variable()
function_with_global_variable()
function_with_parameter("Hola")

# Intentar acceder a una variable local fuera de su ámbito genera un error
# print(local_variable)


'''

Por supuesto, aquí tienes un ejemplo de código en Python que ilustra el concepto de alcance de variables, funciones y el ámbito (scope):

python
Copy code
# Variable global
global_variable = "Soy una variable global"

def function_with_local_variable():
    # Variable local dentro de la función
    local_variable = "Soy una variable local"
    print(local_variable)

def function_with_global_variable():
    # Usar la variable global dentro de la función
    print(global_variable)

def function_with_parameter(parameter):
    # Usar el parámetro de la función
    print("El valor del parámetro es:", parameter)

# Llamada a las funciones
print("Ejemplo de ámbito de variables:")
function_with_local_variable()
function_with_global_variable()
function_with_parameter("Hola")

# Intentar acceder a una variable local fuera de su ámbito genera un error
# print(local_variable)
En este código, puedes observar:

Una variable global llamada global_variable.
Una función function_with_local_variable() que define una variable local llamada local_variable y la imprime.
Una función function_with_global_variable() que imprime la variable global global_variable.
Una función function_with_parameter(parameter) que toma un parámetro y lo imprime.
Las funciones son llamadas al final del código, lo que demuestra cómo las variables pueden tener diferentes alcances en diferentes contextos.
Ten en cuenta que si intentas acceder a una variable local fuera de su función correspondiente, generará un error, ya que su alcance está limitado a esa función.

'''