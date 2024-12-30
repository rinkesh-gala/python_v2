# New operators | and |= allow for merging and updating dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {"above": "list", "below": None}
merged = dict1 | dict2 | dict3
print(merged)