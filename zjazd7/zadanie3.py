class Peekable:

    def __init__(self, iterable):
        self._iterable = iterable
        self._curr_index = 0

    @property
    def iterable(self):
        return self._iterable

    @property
    def curr_index(self):
        return self._curr_index

    def peek(self):
        return self.iterable[self.curr_index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index == len(self.iterable): raise StopIteration
        result = self.iterable[self.curr_index]
        self._curr_index += 1
        return result


peekable = Peekable([1, 2, 3, 4, 5])
print(peekable.peek(), end=' ')
print(next(peekable), end=' ')
print(peekable.peek(), end=' ')
print(peekable.peek(), end=' ')
print(next(peekable), end=' ')
print(peekable.peek(), end=' ')
print('\nAnd the rest...')
for e in peekable:
    print(e)
