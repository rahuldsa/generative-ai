with open("input.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

with open("output.txt", "w") as file:
    file.write(f"Number of words: {word_count}")
