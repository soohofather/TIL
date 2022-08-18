T = int(input())

books_sold = {}


for i in range(T):
    book_name = input()
    if book_name in books_sold:
        books_sold[book_name] += 1
    else:
        books_sold[book_name] = 1

max_value = max(books_sold.values())
max_books = []

for ii in books_sold:
    if books_sold[ii] == max_value:
        max_books.append(ii)
max_books = sorted(max_books)
print(max_books[0])
