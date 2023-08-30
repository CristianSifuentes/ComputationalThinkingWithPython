class ErrorHandler:
    def handle_error(self, error):
        print("An error occurred:", error)

class ZeroDivisionErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("ZeroDivisionError occurred:", error)

class ValueErrorHandler(ErrorHandler):
    def handle_error(self, error):
        print("ValueError occurred:", error)

# Simulación de errores y manejo
def simulate_division_errors(numbers):
    error_handlers = {
        ZeroDivisionError: ZeroDivisionErrorHandler(),
        ValueError: ValueErrorHandler()
    }

    for num_pair in numbers:
        try:
            result = num_pair[0] / num_pair[1]
            print("Result:", result)
        except Exception as error:
            if type(error) in error_handlers:
                handler = error_handlers[type(error)]
                handler.handle_error(error)
            else:
                print("Unhandled error type:", type(error))
        finally:
            print("Finally block executed")

# Ejecutar la simulación
if __name__ == '__main__':
    numbers_to_divide = [(10, 2), (8, 0), (5, 1), (20, 4)]

    simulate_division_errors(numbers_to_divide)
