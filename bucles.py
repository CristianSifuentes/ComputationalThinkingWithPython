# El bucle for en Python
frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
    print(fruta)

print(iter('cadena')) # cadena
print(iter(['a', 'b', 'c'])) # lista
print(iter(('a', 'b', 'c'))) # tupla
print(iter({'a', 'b', 'c'})) # conjunto
print(iter({'a': 1, 'b': 2, 'c': 3})) # diccionario

'''
<str_iterator object at 0x7f385f76ffd0>
<list_iterator object at 0x7f385f76ffd0>
<tuple_iterator object at 0x7f385f76ffd0>
<set_iterator object at 0x7f385f795f80>
<dict_keyiterator object at 0x7f385f785bc0>
'''


frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
print(next(iterador))
print(next(iterador))
print(next(iterador))
'''
manzana
pera
mango
'''


estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)


for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)


for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)
