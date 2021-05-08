lst_num = input().split(", ")
lst_num = list(map(int, lst_num))
end = 10
start = 0
while len(lst_num) > 0:
    a = [n for n in lst_num if start < n <= end]
    print(f"Group of {end}'s: {a}")
    for num in a:
        if num in lst_num:
            lst_num.remove(num)

    end += 10
    start += 10