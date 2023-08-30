def get_value_from_dict(d, key):
    if key in d:
        value = d[key]
        return value
    else:
        return None

def get_element_from_list(lst, index):
    if 0 <= index < len(lst):
        element = lst[index]
        return element
    else:
        return None

def get_nth_element_from_range(rng, n):
    if 0 <= n < len(rng):
        element = rng[n]
        return element
    else:
        return None

if __name__ == '__main__':
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    my_list = [10, 20, 30, 40, 50]
    my_range = range(5)

    # Using LBYL to access elements
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
En este ejemplo, hemos adaptado las mismas funciones 
(get_value_from_dict, get_element_from_list y get_nth_element_from_range) 
para utilizar el principio LBYL. Cada función verifica previamente 
si la clave existe en el diccionario o si el índice es válido para la lista o el rango.

En lugar de manejar las excepciones, como en el principio EAFP, 
el enfoque LBYL se basa en verificar las condiciones antes de realizar 
una operación para evitar excepciones. Si las condiciones no se cumplen, 
las funciones devuelven None.

Aunque LBYL puede ser más explícito en algunos casos y evitar 
excepciones en tiempo de ejecución, puede resultar en 
código más verbose y anidado en comparación con EAFP. 
Además, puede haber problemas de concurrencia en los que 
las condiciones cambien entre la verificación y la operación real.





    '''
