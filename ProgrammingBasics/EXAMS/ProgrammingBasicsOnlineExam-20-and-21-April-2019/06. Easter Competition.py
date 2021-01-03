# Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
import sys
eater_brads = int(input())
for competitors in range(1, eater_brads+1):
    winner = -sys.maxsize
    name = input()
    while name != "Stop":
        grade = int(name)