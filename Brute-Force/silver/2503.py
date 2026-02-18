# 숫자 야구
from itertools import permutations


turn = int(input())
quries, strikes, balls = [], [], []
for _ in range(turn):
    q, s, b = input().split()
    quries.append(q)
    strikes.append(int(s))
    balls.append(int(b))

answers = []
for num in permutations(range(1, 10), 3):
    num = ''.join(map(str, num))
    for q, s, b in zip(quries, strikes, balls):
        # check strike
        num_strikes = 0
        s1, s2 = set(), set()
        for n1, n2 in zip(q, num):
            if n1 == n2:
                num_strikes += 1
            else:
                s1.add(n1)
                s2.add(n2)
        # check ball
        num_balls = len(set(s1) & set(s2))
        if num_strikes != s or num_balls != b:
            break
    else:
        answers.append(num)

print(len(answers))