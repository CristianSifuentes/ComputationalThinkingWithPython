# Singleton pattern using a metaclass
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.data = "Singleton instance data"

# Parent class with a tuple as class attribute
class Parent:
    tup = ("Parent",)

# Child class inheriting from Parent
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.tup = self.tup + ("Child",)

# Function that performs tuple operations and returns a tuple
def tuple_operations(a, b):
    c = a + b
    d = a + b
    e = a * 2
    f = b * 3
    g = b[1]
    return c, d, e, f, g

# Creating instances
singleton_1 = Singleton()
singleton_2 = Singleton()

parent_instance = Parent()
child_instance = Child()

# Tuple operations using the function
result_tuple = tuple_operations((1, 2), (3, 4))

# Displaying instance attributes
print("Singleton 1 data:", singleton_1.data)
print("Singleton 2 data:", singleton_2.data)
print("Parent instance tuple:", parent_instance.tup)
print("Child instance tuple:", child_instance.tup)

# Displaying tuple operations result
print("Tuple operations result:", result_tuple)


'''
En este ejemplo modificado, hemos agregado:

Reasignaciones de Tuplas: En Child se ha reasignado el atributo de tupla para agregar elementos.

Operaciones de Tuplas en Funciones: La función tuple_operations toma dos tuplas como parámetros y realiza sumas, restas y multiplicaciones, y desempaqueta valores de las tuplas para formar una nueva tupla de resultados.

Desempaquetado de Tuplas: Hemos desempaquetado la tupla de resultados en la función tuple_operations al asignar sus elementos a variables individuales.

Retorno de Tuplas en Funciones: La función tuple_operations devuelve una tupla de resultados.

Este ejemplo combina todos estos conceptos avanzados en un solo programa.
'''
