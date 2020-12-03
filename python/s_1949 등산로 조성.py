dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def bfs(y, x):
    for i in range(4):
        ny = y + dc[i]
        nx = x + dr[i]

        if 0 <= ny < N and 0 <= nx < N and li[ny][nx] < li[y][x]:
            stack.append((ny, nx))


    return


T = int(input())

for TC in range(1, T+1):
    N, K = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(N)]

    stack = []
    max_length = 0
    h = 0
    hidx = []
    for i in range(N):
        for j in range(N):
            if li[i][j] > h:
                h = li[i][j]

    for i in range(N):
        for j in range(N):
            if li[i][j] == h:
                hidx.append((i, j))

    for ii in range(N):
        for jj in range(N):
            for k in range(K+1):
                li[ii][jj] -= k
                for i in range(len(hidx)):
                    cnt = 0
                    stack.append(hidx[i])
                    while stack:
                        cnt += 1
                        for _ in range(len(stack)):
                            yx = stack.pop(0)
                            bfs(yx[0], yx[1])
                    if cnt > max_length:
                        max_length = cnt
                        # print(cnt, i, j, ii, jj, k)
                li[ii][jj] += k
    print('#%d %d' % (TC, max_length))