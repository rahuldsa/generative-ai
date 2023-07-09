def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

input_string = "Hello"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)
