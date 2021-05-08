numbers = input().split(" ")
# print(numbers)
string = list(map(str, input()))
# print(sting)
for number in numbers:
    num = list(map(int, number))
    num = sum(num)
    # print(num)
    if len(string) < num:
        num -= len(string)
    else:
        print(string[num], end="")
        string.pop(num)
        continue
    for letter in range(len(string)):
        if letter == num:
            print(string[num],end="")
            string.pop(num)
            break
        if string[letter] == " ":
            print(string[num+1], end="")
            string.pop(num)
            break
