def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

# Example usage:
word = "madam"
if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")
