first_time = int(input())
second_time = int(input())
third_time = int(input())

totall_time = first_time + second_time + third_time
miuti = totall_time // 60
second =  totall_time % 60
if second < 10:
    print(f'{miuti}:0{second}')
else:
    print(f'{miuti}:{second}')



