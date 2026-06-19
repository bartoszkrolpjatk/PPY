from random import randint


def multi_dice(cnt=2):
    yield_counter = 0
    previous_cnt = None
    while True:
        if previous_cnt != cnt: print(f'Throwing {cnt} dice')
        sent = yield yield_counter, tuple([randint(1, 6) for _ in range(cnt)])
        if sent is None:
            yield_counter += 1
        else:
            cnt = sent

        previous_cnt = cnt


g = multi_dice()
next(g)

for _ in range(3):
    print(next(g))

g.send(5)
for _ in range(2):
    print(next(g))

g.send(3)
for _ in range(4):
    print(next(g))
