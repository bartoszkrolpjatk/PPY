# comprehension exercise

# 1. types
lst = [2, {}, 2.3, 'abc', (4,), 2 + 2j]
types = [type(e).__name__ for e in lst]
print(types)

# 2. 0 <= numbers < 10
lst = [[1, 11], [7, -3, 2], [5, 12, -6]]
numbers = [e for l in lst for e in l if 0 <= e <= 10]
print(numbers)

# 3. replace negative with 0 and >10 with 10
lst = [-2, 9, 11, 7, 1, 12, 9]
numbers = [max(min(e, 10), 0) for e in lst]
print(numbers)

# 4. dictionary counting element occurrences
lst = ['Eve', 'Jane', 'Eve', 'Mary', 'John', 'Mary', 'Eve', 'John']
occurrences = {(e, lst.count(e)) for e in set(lst)}
print(occurrences)

# 5. transpose matrix
lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 1, 1, 2]
]
transposed = [[row[i] for row in lst] for i in range(len(lst[0]))]
print(transposed)

# 6. assign color to interval
lst = [87, 102, 90, 117, 95]
colors = ['green' if e < 100 else 'yellow' if e < 115 else 'red' for e in lst]
print(colors)
