# Clase base para una lista mejorada
class EnhancedList(list):
    def __init__(self, *args):
        super().__init__(*args)
    
    def multiply_all_elements(self, factor):
        self[:] = [item * factor for item in self]
    
    def print_with_prefix(self, prefix):
        print(prefix, self)

# Clase derivada con funcionalidad adicional
class AdvancedList(EnhancedList):
    def __init__(self, *args):
        super().__init__(*args)
    
    def remove_duplicates(self):
        self[:] = list(set(self))
    
    def reverse_and_print(self):
        self.reverse()
        print("Reversed:", self)

# Crear una instancia de AdvancedList
my_list = AdvancedList([1, 2, 3, 4, 5, 4, 3, 2, 1])

# Utilizar funciones de la clase derivada
my_list.extend([6, 7, 8])
my_list.insert(0, 0)
my_list.pop()
my_list.remove(3)
my_list.clear()

my_list.extend([5, 3, 9, 2, 7, 1, 4])
my_list.print_with_prefix("Original:")

index = my_list.index(7)
count = my_list.count(2)

print("Index of 7:", index)
print("Count of 2:", count)

my_list.multiply_all_elements(2)
my_list.print_with_prefix("Multiplied:")

my_list.remove_duplicates()
my_list.print_with_prefix("Without Duplicates:")

my_list.sort()
my_list.reverse_and_print()

# Crear una copia de la lista
copied_list = my_list.copy()
print("Copied:", copied_list)
