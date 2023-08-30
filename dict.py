# Definir una fábrica abstracta para crear diccionarios
class DictionaryFactory:
    def create_dictionary(self):
        pass

# Implementar fábricas concretas para diferentes tipos de diccionarios
class RegularDictionaryFactory(DictionaryFactory):
    def create_dictionary(self):
        return {}

class OrderedDictionaryFactory(DictionaryFactory):
    def create_dictionary(self):
        return {}

# Clase base para una operación avanzada en un diccionario
class DictionaryOperation:
    def execute(self, dictionary):
        pass

# Implementar operaciones concretas para los diccionarios
class AddKeyValuePair(DictionaryOperation):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def execute(self, dictionary):
        dictionary[self.key] = self.value

class RemoveKey(DictionaryOperation):
    def __init__(self, key):
        self.key = key
    
    def execute(self, dictionary):
        dictionary.pop(self.key, None)

# Clase que maneja las operaciones en el diccionario
class DictionaryHandler:
    def __init__(self):
        self.dictionary = {}
    
    def perform_operation(self, operation):
        operation.execute(self.dictionary)

# Crear instancias de fábricas concretas
regular_factory = RegularDictionaryFactory()
ordered_factory = OrderedDictionaryFactory()

# Crear instancias de operaciones concretas
add_operation = AddKeyValuePair("name", "John")
remove_operation = RemoveKey("age")

# Crear instancias de manejadores de diccionarios
regular_handler = DictionaryHandler()
ordered_handler = DictionaryHandler()

# Asignar fábricas a los manejadores
regular_handler.factory = regular_factory
ordered_handler.factory = ordered_factory

# Realizar operaciones en los diccionarios
regular_handler.perform_operation(add_operation)
ordered_handler.perform_operation(add_operation)

regular_handler.perform_operation(remove_operation)

# Imprimir los resultados
print("Regular Dictionary:", regular_handler.dictionary)
print("Ordered Dictionary:", ordered_handler.dictionary)

# Más operaciones en diccionarios
regular_handler.dictionary.update({"age": 30, "city": "New York"})
print("Updated Dictionary:", regular_handler.dictionary)

value = regular_handler.dictionary.get("name", "Default")
print("Value for 'name':", value)

del regular_handler.dictionary["city"]
print("Dictionary after 'city' is deleted:", regular_handler.dictionary)

# Iterar a través de las claves y valores en el diccionario
print("Iterating through the dictionary:")
for key, value in regular_handler.dictionary.items():
    print(key, ":", value)

# Crear un nuevo diccionario y sumar los contenidos de ambos
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

summed_dict = {**dict1, **dict2}
print("Summed Dictionary:", summed_dict)


'''
Este código extiende el ejemplo anterior para incluir más operaciones 
de diccionario, como get, del, iteración con for, actualización, 
eliminación y suma de dos diccionarios. Espero que este ejemplo sea 
útil para entender mejor las operaciones que se pueden realizar con diccionarios en Python.
'''