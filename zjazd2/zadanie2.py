from collections import defaultdict
from itertools import groupby

names = ["John", "Mary", "Kitty", "Alice", "John", "Mary", "Al", "Bill", "John", "Alice", "Al"]

#list-comprehension
lengths = [len(e) for e in names]
print("Lengths: ", lengths)

#defaultdict class
length_names_list = defaultdict(list)
for name in names:
    length_names_list[len(name)].append(name)
print("Length:[names] dictionary ", length_names_list)

#groupby class
sorted_names = sorted(names, key=len)
lengths_names_set = {key: set(val) for key, val in groupby(sorted_names, key=len)}
print(lengths_names_set)

#regular for-loop
