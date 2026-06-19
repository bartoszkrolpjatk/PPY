import time

class Timer:
    success = False

    def __init__(self):
        self.start = None

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    def __enter__(self):
        self.start = time.perf_counter_ns()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            Timer.success = True
            print(f'Time {time.perf_counter_ns() - self.start}ns', end=' ')
        else :
            Timer.success = False
            print(f'{exc_type.__name__} N negative! No result')

        return True




def fibo(n):
    if n < 0: raise ValueError;
    if n <= 1: return n
    return fibo(n-1) + fibo(n-2)

for n in (13, -1, 11, 12, 16, -9, 20):
    print(f'N = {n:2d} ', end='')
    with Timer():
        res = fibo(n)
    if Timer.success: print(f'res={res:>10d}')