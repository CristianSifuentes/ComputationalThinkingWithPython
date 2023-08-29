from abc import ABC, abstractmethod

class AbstractFactorialFactory(ABC):
    @abstractmethod
    def create_factorial(self):
        pass

class RecursiveFactorialFactory(AbstractFactorialFactory):
    def create_factorial(self):
        return RecursiveFactorial()

class Factorial(ABC):
    @abstractmethod
    def calculate(self, n):
        pass

class RecursiveFactorial(Factorial):
    def calculate(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calculate(n - 1)

def calculate_factorial(factory, n):
    factorial = factory.create_factorial()
    return factorial.calculate(n)

# Test the factorial calculation using RecursiveFactorialFactory
factory = RecursiveFactorialFactory()
number = 5
result = calculate_factorial(factory, number)
print(f"The factorial of {number} is {result}")