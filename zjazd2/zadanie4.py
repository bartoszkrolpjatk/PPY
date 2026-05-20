from collections import defaultdict

dct = {'John': 3, 'Bill': 4, 'Jane': 4, 'Kim': 2,
       'Mary': 3, 'Joe': 0, 'Sue': 5, 'Ada': 2, 'Ray': 2}

wins_names_list = defaultdict(list)
for key, val in dct.items():
       wins_names_list[val].append(key)

print(*wins_names_list.items(), sep="\n", end="\n\n")

sorted_by_wins = sorted(wins_names_list.items(), key=lambda item : item[0], reverse=True)
print(*sorted_by_wins, sep="\n")