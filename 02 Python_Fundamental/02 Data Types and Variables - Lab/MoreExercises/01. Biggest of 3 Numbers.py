first_num = int(input())
second_num = int(input())
third_num = int(input())
biggest = [first_num, second_num, third_num]
biggest.sort(reverse=True)
print(biggest[0])
