def factorial(number):
    if number == 0 or number == 1:
        return 1
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

input_number = 5
factorial_result = factorial(input_number)
print("Factorial of", input_number, "is", factorial_result)
