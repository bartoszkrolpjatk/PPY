import heapq


def multimerge(*args):
    yield from heapq.merge(*args)



lst = [[2, 3, 12], [], [8, 9], [4], [3, 8, 9, 10, 13]]
g = multimerge(*lst)
print(list(g))