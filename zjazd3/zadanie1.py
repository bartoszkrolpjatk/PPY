from functools import reduce


def create_input_tuple(user_input):
    split = tuple(map(int, user_input.split()))
    mul = lambda x, y: x * y
    match len(split):
        case 1:
            return "S", split, split[0] ** 2
        case 2:
            return "R", split, reduce(mul, split, 1)
        case 3:
            return "C", split, reduce(mul, split, 1)
        case _:
            raise ValueError("invalid number of input numbers")


res = list()
while True:
    try:
        text_input = input("Enter 1, 2 or 3 numbers: ")
        if not text_input.strip():
            break
        res.append(create_input_tuple(text_input))
    except ValueError as e:
        print(f"Invalid input: {e}")

print(res)
