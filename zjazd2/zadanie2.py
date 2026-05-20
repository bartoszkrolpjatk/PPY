from collections import defaultdict, Counter
from itertools import groupby

names = ["John", "Mary", "Kitty", "Alice", "John", "Mary", "Al", "Bill", "John", "Alice", "Al"]

#list-comprehension
lengths = [len(e) for e in names]
print("Lengths: ", lengths)

#defaultdict class
length_names_list = defaultdict(list)
for name in names:
    length_names_list[len(name)].append(name)
print("Length:[names list] (defaultdict)", length_names_list)

#groupby class
sorted_names = sorted(names, key=len)
lengths_names_set = {key: set(val) for key, val in groupby(sorted_names, key=len)}
print("Length: {names set} (groupby)", lengths_names_set)

#regular for-loop
name_times = {}
for name in names:
    if name not in name_times:
        name_times[name] = 0
    name_times[name] = name_times[name] + 1
print("Name: times occurred (regular for)", name_times)

#Counter class
name_times = Counter(names)
print("Name: times occurred (Counter)", name_times)