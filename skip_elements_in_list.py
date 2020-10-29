
# This is propram to skip some items from list

def skip_elements(elements):
    # Initialize variables
    new_list = []
    if len(elements) == 0:
        return new_list

    # Iterate through the list
    for i in range(0, len(elements) + 1, 2):
        if not elements[i] in new_list:
            new_list.append(elements[i])

    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Pineapple', 'Pineapple', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']



