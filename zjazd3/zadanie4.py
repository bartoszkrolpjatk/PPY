from collections import defaultdict

bibliophiles = {
    'John': {1, 2, 7, 11, 29},
    'Mary': {7, 9, 11, 5},
    'Jane': {1, 4, 5},
    'Bill': {7, 11, 1, 2, 9},
    'Kate': {4, 5, 9, 11}
}

# returns a 3-element tuple, takes in bibliophiles and person to compare to
# 1 element is person that shares the most numbers of books with person to compare
# 2 element is number of shared books
# 3 element is set of books person from first parameter read but person to compare did not
def compare_common(to_compare, dic):
    to_compare_books = dic[to_compare]
    shared_books_with = defaultdict(int)
    to_check = ((k, v) for k, v in dic.items() if k != to_compare)

    for key, val in to_check:
        shared_books_with[key] = len((to_compare_books & val))

    most_common_person, num_shared = max(shared_books_with.items(), key=lambda item: item[1])
    return most_common_person, num_shared, dic[most_common_person] - to_compare_books

print(compare_common('John', bibliophiles))
print(compare_common('Mary', bibliophiles))

# returns a 2-element tuple, takes in bibliophiles and person to compare to
# 1 element is the most popular book that to_compare person owns
# 2 element is a list of people owning the book
def compare_popular(to_compare, dic):
    to_compare_books = dic[to_compare]
    book_popularity = defaultdict(int)
    to_check = ((k, v) for k, v in dic.items() if k != to_compare)

    for name, books in to_check:
        for book in to_compare_books:
            book_popularity[book] += 1 if book in books else 0

    most_popular_book, owners_count = max(book_popularity.items(), key=lambda item: item[1])
    return most_popular_book, owners_count

print(compare_popular('John', bibliophiles))
print(compare_popular('Jane', bibliophiles))



# returns a 2-element tuple, takes in bibliophiles and person to compare to
# 1 element is the most popular book that to_compare person does not own
# 2 element is a list of people owning the book
def compare_popular_not_owned(to_compare, dic):
    book_popularity = defaultdict(int)
    to_check = ((k, v) for k, v in dic.items() if k != to_compare)

    for name, books in to_check:
        for book in books:
            book_popularity[book] += 1

    not_owned = book_popularity.keys() - dic[to_compare]

    most_popular_book = max(not_owned, key=lambda b: book_popularity[b])
    return most_popular_book, book_popularity[most_popular_book]

print(compare_popular_not_owned('John', bibliophiles))
print(compare_popular_not_owned('Kate', bibliophiles))