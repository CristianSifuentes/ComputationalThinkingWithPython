class ErrorHandler:
    def handle_error(self, error):
        print("An error occurred:", error)

class ImportErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("ImportError occurred:", error)

class IndexErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("IndexError occurred:", error)

class NameErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("NameError occurred:", error)

class SyntaxErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("SyntaxError occurred:", error)

class TypeErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("TypeError occurred:", error)

class ValueErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("ValueError occurred:", error)

# Simulación de errores y manejo
def simulate_errors():
    error_handlers = {
        ImportError: ImportErrorHandler(),
        IndexError: IndexErrorHandler(),
        NameError: NameErrorHandler(),
        SyntaxError: SyntaxErrorHandler(),
        TypeError: TypeErrorHandler(),
        ValueError: ValueErrorHandler()
    }

    errors = [
        (ImportError, "Module not found"),
        (IndexError, "List index out of range"),
        (NameError, "Variable not defined"),
        (SyntaxError, "Invalid syntax"),
        (TypeError, "Unsupported operand type"),
        (ValueError, "Invalid value")
    ]

    for error_type, error_message in errors:
        try:
            raise error_type(error_message)
        except Exception as error:
            if error_type in error_handlers:
                handler = error_handlers[error_type]
                handler.handle_error(error)
            else:
                print("Unhandled error type:", error_type)
        finally:
            print("Finally block executed")

# Ejecutar la simulación
if __name__ == '__main__':
    simulate_errors()


'''
En esta versión, hemos utilizado un diccionario error_handlers para 
asociar cada tipo de error con su respectivo manejador. 
Hemos modificado la estructura de errors para que sea una 
lista de tuplas, donde cada tupla contiene el tipo de error y el mensaje de error.

Dentro del bucle simulate_errors, usamos un bloque try para 
lanzar el tipo de error correspondiente con su mensaje. 
En el bloque except, verificamos si el tipo de error tiene un 
manejador asociado en el diccionario error_handlers, y si es así, 
llamamos al método handle_error del manejador.

Finalmente, en el bloque finally, se imprime un mensaje 
indicando que el bloque finally se ejecutó independientemente 
de si se lanzó una excepción o no. Esto se hace para resaltar 
el uso del bloque finally en el manejo de excepciones.

'''