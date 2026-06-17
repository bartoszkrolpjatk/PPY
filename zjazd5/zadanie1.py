def rm_adj_dup(seq):
    previous = None
    for el in seq:
        if el != previous:
            yield el
            previous = el


ls = [1, 1, 4, 5, 5, 5, 2, 1, 5, 5]
gen = rm_adj_dup(ls)
for e in gen: print(e, end=' ')
print('\ntype(gen):', type(gen).__name__)