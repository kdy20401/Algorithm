# 일곱 난쟁이

from itertools import combinations


talls = []
for _ in range(9):
    t = int(input())
    talls.append(t)

combs = list(combinations(talls, 7))
for comb in combs:
    if sum(comb) == 100:
        break

for t in sorted(comb):
    print(t)