def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Example usage:
people = {}
add_person(people, "John", 25)
update_age(people, "John", 26)
delete_person(people, "John")
print(people)
