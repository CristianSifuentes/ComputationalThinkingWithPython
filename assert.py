def calculate_square_root(x):
    assert x >= 0, "Cannot calculate square root of a negative number"
    return x ** 0.5

def find_substring(text, substring):
    assert len(substring) > 0, "Substring cannot be empty"
    index = text.find(substring)
    assert index != -1, f"Substring '{substring}' not found in '{text}'"
    return index

if __name__ == '__main__':
    try:
        number = float(input("Enter a non-negative number: "))
        result = calculate_square_root(number)
        print("Square root:", result)
    except ValueError as e:
        print("Error:", e)

    text = "Hello, world! This is a test string."
    substring = input("Enter a substring to search for: ")

    try:
        index = find_substring(text, substring)
        print(f"Substring '{substring}' found at index {index}")
    except AssertionError as e:
        print("Error:", e)


'''
En este ejemplo, la función calculate_square_root calcula 
la raíz cuadrada de un número no negativo utilizando una 
afirmación para asegurarse de que el número sea no negativo
antes de realizar el cálculo. Si el número es negativo, la 
afirmación lanzará una excepción con un mensaje personalizado.

La función find_substring busca un substring en un texto 
utilizando la afirmación para asegurarse de que el substring 
no esté vacío. Luego, utiliza text.find(substring) para buscar 
el substring en el texto. Si el substring no se encuentra, 
la afirmación lanzará una excepción con un mensaje personalizado.

En el bloque __main__, el programa solicita un número no 
negativo para calcular su raíz cuadrada y también un substring
 para buscar en el texto. Si se producen errores en las afirmaciones, 
 se capturan y manejan adecuadamente para imprimir mensajes de error explicativos.

'''