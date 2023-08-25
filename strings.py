my_str = 'String'
print(len(my_str))

print(my_str[0]) # S
print(my_str[1]) # t
print(my_str[2]) # r
print(my_str[3]) # i
print(my_str[2:]) # ring
print(my_str[:3]) # Str
print(my_str[:3]) # Str
print(my_str[:3]) # Str
print(my_str[:-2]) # Stri
print(my_str[::2]) # Srn
print('This is a example using ' + my_str) # This is a example using String
print(f'This is a example using {my_str}') # This is a example using String
print(f'This is a example using {my_str}' * 100)

nombre = input('Cual es tú nombre: ')
print(nombre)
print('Tú nombre es ', nombre)
print(f'Tú nombre es  {nombre}')
numero = input('Escribe un entero: ')
print(type(numero))
numero = int(numero)
print(type(numero))


frase = 'python es un gran lenguaje'

# para saber cuantas veces aparece un caracter en nuestro string usamos la funcion count.

print(frase.count('e'))

# si queremos reemplazar un caracter por otro usamos la funcion replace usando la logica: frase.replace('letra a cambiar', 'letra nueva').
print(frase.replace('p', 'q'))

# para separar nuestra string en una lista con todos los string segun un patron como el espacio entre palabras hacemos 

print(frase.split(' ')) 




