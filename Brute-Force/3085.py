# 사탕 게임

# 한 행 또는 열에 대해 가장 긴 연속된 사탕 길이를 구하는 연산: N^2
# 바꿀 때마다 3번 연산
# 바꾸는 총 횟수: N^2 * 2 (가로 방향, 세로 방향 바꾸기)
# 총 계산: 6 * N^4 (< 40000000)

def get_longest_consecutive(lst):
    max_length = 1
    cur_length = 1
    # abb
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                cur_length += 1
            else:
                max_length = max(max_length, cur_length)
                cur_length = 1
                break
        max_length = max(max_length, cur_length)
        cur_length = 1

    return max_length

N = int(input())
board = []
for _ in range(N):
    inp = input()
    row = []
    for s in inp:
        row.append(s)
    board.append(row)

answer = 1
# 1. swap between left and right
for i in range(N):
    for j in range(N):
        if j < N - 1 and board[i][j] != board[i][j + 1]:
            # swap
            temp = board[i][j]
            board[i][j] = board[i][j + 1]
            board[i][j + 1] = temp

            # row
            r1 = get_longest_consecutive(board[i])
            # col1, col2
            c1 = get_longest_consecutive([board[k][j] for k in range(N)])
            c2 = get_longest_consecutive([board[k][j + 1] for k in range(N)])
            m = max([r1, c1, c2])

            answer = max(answer, m)

            # swap
            temp = board[i][j]
            board[i][j] = board[i][j + 1]
            board[i][j + 1] = temp

# 2. swap between up and down
for i in range(N):
    for j in range(N):
        if j < N - 1 and board[j][i] != board[j + 1][i]:
            # swap
            temp = board[j][i]
            board[j][i] = board[j + 1][i]
            board[j + 1][i] = temp

            # col
            c1 = get_longest_consecutive([board[k][i] for k in range(N)])
            # row1, row2
            r1 = get_longest_consecutive(board[j])
            r2 = get_longest_consecutive(board[j + 1])
            m = max([c1, r1, r2])

            answer = max(answer, m)

            # swap
            temp = board[j][i]
            board[j][i] = board[j + 1][i]
            board[j + 1][i] = temp

# 3. check all rows and cols (스왑 안해도 해당 행이나 열이 최대값을 포함하는 경우)
for i in range(N):
    answer = max(answer, get_longest_consecutive(board[i]))
    answer = max(answer, get_longest_consecutive([board[k][i] for k in range(N)]))

print(answer)