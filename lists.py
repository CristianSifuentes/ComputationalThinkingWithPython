# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Mostrar la lista original
print("Lista original:", numeros)

# Modificar un elemento en la lista
numeros[2] = 10
print("Lista después de modificar:", numeros)

# Sumar todos los elementos de la lista
suma_total = sum(numeros)
print("Suma total:", suma_total)

# Restar 5 a todos los elementos de la lista usando comprensión de listas
numeros_resta = [num - 5 for num in numeros]
print("Resta 5:", numeros_resta)

# Multiplicar todos los elementos de la lista por 2 usando un bucle
numeros_multiplicados = []
for num in numeros:
    numeros_multiplicados.append(num * 2)
print("Multiplicación por 2:", numeros_multiplicados)

# Dividir todos los elementos de la lista por 3 usando función map y lambda
numeros_divididos = list(map(lambda x: x / 3, numeros))
print("División por 3:", numeros_divididos)


'''
En este ejemplo, creamos una lista de números y demostramos cómo modificar elementos en la lista.
 Luego, realizamos operaciones como suma, resta, multiplicación y división en los elementos
   de la lista utilizando diferentes enfoques. Esto te ayudará a comprender cómo las listas 
   son mutables y cómo puedes manipular sus elementos para realizar diversas operaciones.
'''
