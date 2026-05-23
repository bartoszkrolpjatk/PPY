#goal of each exercise is to analyze the output without executing the program

lst = [(1, 'Bob'), (4, 'Alicia'), (3, 'John')]
print(sorted(lst, key=lambda t: -t[0])[-3][1])
#Alicia

a, b, c = 2, 5, 8
print(a < c < b,  a != c > 1,  b < a > c)
#False, True, False

lst = [1, 2, [4, 5], 7]
print(id(lst), id(lst[1]), id(lst[0]), id(lst[2]))
lst[0] = lst[1] = 8
lst[2].append(6)
print(id(lst), id(lst[1]), id(lst[0]), id(lst[2]))

a, b, c = {1, 2, 3, 4}, {3, 4, 5}, {1, 5, 7}
print(a - b & c)

def fun(val, lst=[]):
    lst.append(val)
    return lst

print(fun(1))
print(fun(2, []))
print(fun(3))