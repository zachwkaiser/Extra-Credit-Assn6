# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        return "Cannot divide by 0."
    return a / b  # Potential division by zero error

def multiply_numbers(a, b):
    """Multiplies two numbers"""

    return a * b
if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    mult_result = multiply_numbers(x, y)
    print(f"The result of division is: {result}")
    print(f"The result of multiplication is: {mult_result}")
