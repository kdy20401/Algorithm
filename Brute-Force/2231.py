# 분해합

N = int(input())
for n in range(1, N + 1):
    a = 0
    a += n
    for j in str(n):
        a += int(j)
    if a == N:
        print(n)
        break
else:
    print(0)