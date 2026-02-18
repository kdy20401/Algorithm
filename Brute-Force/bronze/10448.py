# 유레카 이론

from itertools import combinations

# 삼각 수: n*(n+1)/2 => 1, 3, 6, 10, 15, 21,,,
# n*(n+1) <= 2000
# 총 약 50개
# 완탐 => 50^3

def f(n, tri_nums):
    for i in tri_nums:
        for j in tri_nums:
            for k in tri_nums:
                if i + j + k == n:
                    return 1
    return 0

T = int(input())
tri_nums = []
for i in range(1, 50):
    tri_nums.append(i * (i + 1) // 2)

while T:
    n = int(input())
    answer = f(n, tri_nums)
    print(answer)
    T -= 1