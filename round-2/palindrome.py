def is_palindrome_number(number):
    number_str = str(number)
    return number_str == number_str[::-1]


print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
