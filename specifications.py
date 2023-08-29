def calculate_square(number):
    """
    This function calculates the square of a given number.
    
    Parameters:
        number (int): The number for which the square will be calculated.
        
    Returns:
        int: The square of the input number.
    """
    square = number ** 2
    return square

def calculate_cube(number):
    """
    This function calculates the cube of a given number.
    
    Parameters:
        number (int): The number for which the cube will be calculated.
        
    Returns:
        int: The cube of the input number.
    """
    cube = number ** 3
    return cube

# Viewing the docstring using the help() function
help(calculate_square)
help(calculate_cube)
'''
En este ejemplo, cada función tiene un docstring que describe el 
propósito de la función, los parámetros que toma y el valor de 
retorno que produce. Puedes ver la documentación de una función 
utilizando la función help(). Simplemente ejecuta el código 
en un entorno de Python (como en la terminal o en un archivo .py) y
luego ejecuta help(calculate_square) o help(calculate_cube) para ver 
la documentación de la función correspondiente.

'''





