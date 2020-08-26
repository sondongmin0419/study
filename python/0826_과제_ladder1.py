import sys
sys.stdin = open("input.txt", "r")


def ladder(y, x, tmp):  # 세로 가로 이전가로
    test = []
    if x != 0 and x != N-1:
        test = li[y][x-1:x+2]
        if test[0] == 1 and (x-1) != tmp:
            return y, x-1, x
        elif test[2] == 1 and (x+1) != tmp:
            return y, x+1, x
    elif x == 0:
        test = li[y][x:x + 2]
        if test[1] == 1 and (x + 1) != tmp:
            return y, x+1, x
    elif x == N-1:
        test = li[y][x-1:x + 1]
        if test[0] == 1 and (x - 1) != tmp:
            return y, x-1, x
    if y == 0:
        return y, x, x
    return y-1, x, x



N = 100
T = 10
for TC in range(1, T+1):
    tc = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    i = N-1
    j = 0
    b_j = 0

    for k in range(N):
        if li[N-1][k] == 2:
            j = k
            b_j = k
            break

    while i >= 1:
        a, b, c = ladder(i, j, b_j) # 세로 가로 이전가로
        i, j, b_j = a, b, c

    print(f'#{tc} {j}')




