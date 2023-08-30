def get_value_from_dict(d, key):
    try:
        value = d[key]
        return value
    except KeyError:
        return None

def get_element_from_list(lst, index):
    try:
        element = lst[index]
        return element
    except IndexError:
        return None

def get_nth_element_from_range(rng, n):
    try:
        element = rng[n]
        return element
    except IndexError:
        return None

if __name__ == '__main__':
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    my_list = [10, 20, 30, 40, 50]
    my_range = range(5)

    # Using EAFP to access elements
    key = 'key2'
    index = 3
    n = 2

    value_from_dict = get_value_from_dict(my_dict, key)
    element_from_list = get_element_from_list(my_list, index)
    nth_element_from_range = get_nth_element_from_range(my_range, n)

    print("Value from dict:", value_from_dict)
    print("Element from list:", element_from_list)
    print("Nth element from range:", nth_element_from_range)


'''
En este ejemplo, hemos creado tres funciones 
(get_value_from_dict, get_element_from_list y get_nth_element_from_range) que 
utilizan el principio EAFP. Cada función intenta acceder a un 
valor específico en un diccionario, una lista o un rango, 
respectivamente. Si la operación falla debido a una excepción 
(KeyError o IndexError), las funciones devuelven None.

Luego, en el bloque __main__, creamos un diccionario, 
una lista y un rango, y utilizamos las funciones EAFP 
para acceder a valores y elementos específicos. Si el 
acceso no tiene éxito, las funciones devolverán None.

Este enfoque EAFP evita la necesidad de comprobar 
previamente si las claves existen en los diccionarios 
o si los índices son válidos en las listas o rangos, 
lo que resulta en un código más limpio y legible.
    
    '''
