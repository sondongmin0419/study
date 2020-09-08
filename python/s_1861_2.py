import sys
sys.setrecursionlimit(10000)
sys.stdin = open("input_3.txt", "r")

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def delyx(y, x, s_n):
    global cnt
    global max_n
    global max_s_n
    stack.append(li[y][x])

    li_v[y][x] = 1

    cnt += 1
    for i in range(4):
        ny = y + dc[i]
        nx = x + dr[i]
        if 0 <= ny < N and 0 <= nx < N and abs(li[ny][nx]-li[y][x]) == 1 and li_v[ny][nx] == 0:
            delyx(ny, nx, s_n)
    if cnt > max_n:
        max_n = cnt
        min_s = min(stack)
        max_s_n = min_s
    elif cnt == max_n:
        min_s = min(stack)
        if max_s_n > min_s:
            max_s_n = min_s

    return


T = int(input())

for TC in range(1, T+1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]
    li_v = [[0] * N for _ in range(N)]
    li_max = [[0] * N for _ in range(N)]
    max_n = 0
    start_n = 0
    max_s_n = 10**3
    cnt = 0
    for i in range(N):
        for j in range(N):
            stack = []

            cnt = 0
            start_n = li[i][j]
            delyx(i, j, start_n)

    print('#%d %d %d' % (TC, max_s_n, max_n))