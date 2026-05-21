from collections import defaultdict

def find_most_popular(lst):
    times_occurred = defaultdict(int)
    most_popular_element = None
    max_occurrences = 0
    for el in lst:
        times_occurred[el] += 1
        if times_occurred[el] >= max_occurrences:
            most_popular_element = el
            max_occurrences = times_occurred[el]
    return most_popular_element, max_occurrences

numbers = [-4, 0, 3, -4, 2, -4, -3, 3, 2]
chars = 'to be or not to be'.split()

print(find_most_popular(numbers))
print(find_most_popular(chars))

