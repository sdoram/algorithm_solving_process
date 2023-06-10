# https://www.acmicpc.net/problem/1302
book_dict = {}
for _ in range(int(input())):
    book = input()
    if book not in book_dict:
        book_dict[book] = 1
    else:
        book_dict[book] += 1
book_dict = sorted(book_dict.items())
book_dict = sorted(book_dict, key=lambda x: x[1], reverse=True)
print(book_dict[0][0])
