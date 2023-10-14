original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_keep = ['a', 'c', 'e']

# Create a new dictionary by filtering the original dictionary
new_dict = {key: original_dict[key] for key in original_dict if key in keys_to_keep}

# Print the new dictionary
print(new_dict)