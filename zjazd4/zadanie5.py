from functools import reduce

m = [
    [10, 20, 3],
    [2, 3, 4, 5, 6],
    [20, 20, 25, 0, -15]
]
minave = 10

lst = [(i, avg) for i, row in enumerate(m) for avg in [sum(row)/len(row)] if avg >= minave]
print(lst)
