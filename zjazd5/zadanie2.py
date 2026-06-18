from collections import deque


def sliding_window(seq, width):
    window = deque([], width)
    for e in seq:
        window.append(e)
        if len(window) < width : continue
        yield tuple(window)
    if len(window) < width:
        window.extend([None] * (width - len(window)))
        yield tuple(window)


lst = [1, 2, 3, 4, 5]
g = sliding_window(lst, 3)
print(list(g))

g = sliding_window(lst, 5)
print(list(g))
g = sliding_window(lst, 7)
print(list(g))


def helper():
    for n in range(1, 6): yield n

g = sliding_window(helper(), 4)
print(list(g))
