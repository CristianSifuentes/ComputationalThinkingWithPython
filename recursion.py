def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    Parameters:
        n (int): The number for which the factorial will be calculated.
        
    Returns:
        int: The factorial of the input number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        print("n", n)
        return n * factorial(n - 1)

# Test the factorial function
number = 10
result = factorial(number)
print(f"The factorial of {number} is {result}")
