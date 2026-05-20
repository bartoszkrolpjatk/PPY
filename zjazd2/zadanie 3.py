from collections import Counter

n = int()
while True:
    try:
        n = int(input("Enter list length: "))
        break
    except ValueError:
        print("Invalid input")

uq_numbers = set()
duplicates = set()
all_numbers = [] #for the case of Counter usage
while len(uq_numbers) < n:
    while True:
        try:
            new_number = int(input("Enter element: "))
            if new_number in uq_numbers:
                duplicates.add(new_number)
            uq_numbers.add(new_number)
            all_numbers.append(new_number) #for the case of Counter usage
            break
        except ValueError:
            print("Invalid input")

print("All given numbers: ", uq_numbers)
print("Duplicated numbers: ", duplicates)

duplicates = [key for key, val in Counter(all_numbers).items() if val > 1]
print("Duplicated numbers (Counter): ", duplicates)
