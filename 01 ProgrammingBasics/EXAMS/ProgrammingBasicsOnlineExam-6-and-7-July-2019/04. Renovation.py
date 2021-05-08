# 1.	Височина на стената - цяло число [0… 100]
# 2.	Ширина на стената - цяло число [0… 100]
# 3.	Процент от общата площ на стените, който няма да бъде боядисан - цяло число [5… 95]
# На следващите редове до получаване на командата "Tired!" или докато не бъдат боядисани всички стени, се чете по едно число:
# •	Литри боя – цяло число [0…100]:
# Забележка: Площта за боядисване да бъде закръглена нагоре до най-близкото цяло число.
import sys
hight = int(input())
weight = int(input())
persentage = int(input())

total_space = (hight * weight * 4) - (hight * weight * 4 /100 * persentage)
command = input()

while command != 'Tired!':
    litra_current = int(command)
    total_space -= litra_current
    if total_space > 0:
        command = input()
        continue
    else:
        if total_space == 0:
            print(f"All walls are painted! Great job, Pesho!")
            sys.exit(0)
        if total_space < 0:
            print(f"All walls are painted and you have {round(abs(total_space))} l paint left!")
            sys.exit(0)

print(f"{round(total_space)} quadratic m left.")