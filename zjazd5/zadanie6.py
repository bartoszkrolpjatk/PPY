import functools


def primed(gene):
    @functools.wraps(gene)
    def wrapper(*args, **kwargs):
        f = gene(*args, **kwargs)
        next(f)
        return f

    return wrapper


@primed
def rpn(target):
    stack = []
    while True:
        el = yield
        if el == 'end':
            target.send(stack.pop())
            stack.clear()
        else:
            if isinstance(el, (int, float)):
                stack.append(el)
            else:
                second = stack.pop()
                first = stack.pop()
                match el:
                    case '+':
                        stack.append(first + second)
                    case '-':
                        stack.append(first - second)
                    case '*':
                        stack.append(first * second)
                    case '/':
                        stack.append(first / second)
                    case _:
                        raise ValueError("Illegal character: ", el)


@primed
def to_list(target):
    while True:
        el = yield
        target.append(el)


def gen(source, target):
    for e in source: target.send(e)


src = [5, 7, '+', 2, '*', 20, '-', 'end',
       7, 2, '-', 2, 1, '+', '/', 3, '*', 5, '+', 'end',
       5, 2, '-', 2.5, 2, '*', '*', 13.5, '-', 'end']
lst = []
gen(src, rpn(to_list(lst)))
print('Results:', lst)
