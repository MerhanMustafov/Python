searched_book = input()
wrong_once = 0
book_is_found = False
current_book = input()
while current_book != 'No More Books':

    if current_book == searched_book:
        book_is_found = True
        print(f"You checked {wrong_once} books and found it." )
        break
    wrong_once += 1
    current_book = input()
if not book_is_found:
    print("The book you search is not here!")
    print(f"You checked {wrong_once} books.")


# book_counter = 0
# isFound = False
#
# searched_book = input()
# next_book = input()
#
# while next_book != 'No More Books':
#     if next_book == searched_book:
#         isFound = True
#         break
#     book_counter +=1
#     next_book = input()
#
# if isFound:
#     print(f"You checked {book_counter} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {book_counter} books.")
