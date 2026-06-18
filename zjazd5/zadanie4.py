from functools import wraps

def primeIt(func):
    @wraps(func)
    def primed(*args, **kwargs):
        p = func(*args, **kwargs)
        next(p)
        return p
    return primed

@primeIt
def runningAverage():
    numbers = []
    new = None
    while True:
        if new is None and numbers:
            numbers.clear()
        new = yield sum(numbers) / len(numbers) if numbers else 0
        numbers.append(new)


coro = runningAverage()
print( coro.send(2) )
print( coro.send(4) )
print( coro.send(6) )
print('*resetting*')
coro.send(None)
print( coro.send(9) )
print( coro.send(1) )
print( coro.send(8) )
