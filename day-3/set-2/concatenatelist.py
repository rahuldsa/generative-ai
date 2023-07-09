list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenated_list = []

for item1 in list1:
    for item2 in list2:
        concatenated_list.append(item1 + item2)

print(concatenated_list)
