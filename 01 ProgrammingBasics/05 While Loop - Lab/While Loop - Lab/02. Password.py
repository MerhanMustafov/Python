userName = input()
password = input()
correct = input()
while correct != password:
    correct = input()
else:
    print(f'Welcome {userName}!')