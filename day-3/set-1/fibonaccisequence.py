def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

input_number = 5
fibonacci_sequence = fibonacci(input_number)
print(fibonacci_sequence)
