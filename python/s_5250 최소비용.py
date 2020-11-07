dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def min_f(x, y, li_f):
    global f
    global result_f
    if f > result_f:
        return
    if x == N - 1 and y == N - 1:
        if f < result_f:
            result_f = f
            return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < N and 0 <= nx < N and li_f[ny][nx] == 0:
            if li[ny][nx] > li[y][x]:
                f += li[ny][nx] - li[y][x]
            f += 1
            li_f[ny][nx] = 1
            min_f(nx, ny, li_f)
            if li[ny][nx] > li[y][x]:
                f -= li[ny][nx] - li[y][x]
            f -= 1
            li_f[ny][nx] = 0


T = int(input())

for TC in range(1, T + 1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    li_f = [[0] * N for _ in range(N)]
    f = 0
    result_f = 100 * 100 * 1000

    min_f(0, 0, li_f)
    print('#%d %d' % (TC, result_f))
