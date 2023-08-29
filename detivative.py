from abc import ABC, abstractmethod

# Abstract Factory
class DerivativeFactory(ABC):
    @abstractmethod
    def create_derivative(self):
        pass

# Concrete Factory
class PowerRuleFactory(DerivativeFactory):
    def create_derivative(self):
        return PowerRuleDerivative()

class Derivative(ABC):
    @abstractmethod
    def calculate(self, expression):
        pass

# Concrete Product
class PowerRuleDerivative(Derivative):
    def calculate(self, expression):
        # Assuming expression is of the form 'ax^n'
        parts = expression.split('*')
        coefficient = int(parts[0])
        exponent = int(parts[1].split('^')[1])
        
        new_coefficient = coefficient * exponent
        new_exponent = exponent - 1
        
        if new_exponent == 0:
            return str(new_coefficient)
        else:
            return f"{new_coefficient}*x^{new_exponent}"

def calculate_derivative(factory, expression):
    derivative = factory.create_derivative()
    return derivative.calculate(expression)

# Test the derivative calculation using PowerRuleFactory
factory = PowerRuleFactory()
expression = "3*x^4"
result = calculate_derivative(factory, expression)
print(f"The derivative of {expression} is {result}")
