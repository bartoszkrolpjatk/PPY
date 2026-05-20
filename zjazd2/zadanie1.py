def is_even(num):
    return num % 2 == 0

def fulfilled_elements(pred, l):
    res = []
    for el in l:
        if pred(el):
            res.append(el)
    return res

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input")

first_el = 1
step = 3
last_el = step * n + first_el
lst = list(range(first_el, last_el, step))
print(lst)

are_even = [e for e in lst if is_even(e)]
print(are_even)

are_even = list(filter(is_even, lst))
print(are_even)

print(fulfilled_elements(is_even, lst))
print(fulfilled_elements(lambda e: e % 2 != 0, lst))