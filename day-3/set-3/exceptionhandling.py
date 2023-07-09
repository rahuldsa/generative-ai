def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Example usage:
a = 5
b = 0
result = divide_numbers(a, b)
print(result)
