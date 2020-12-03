d = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def play():
    stack = []
    for i in range(N):
        for j in range(N):
            if len(li[i][j]) > 1:
                n = 0
                m = 0
                total = 0
                for _ in range(len(li[i][j])):
                    t_li = li[i][j].pop(0)
                    if t_li[0] > n:
                        n = t_li[0]
                        m = t_li[1]
                    total += t_li[0]
                li[i][j].append([total, m])
            if li[i][j]:
                ny = d[li[i][j][0][1] - 1][0] + i
                nx = d[li[i][j][0][1] - 1][1] + j
                if ny == 0 or ny == N - 1:
                    # li[ny][nx].append([li[i][j][0][0] // 2, li[i][j][0][1] % 2 +1])
                    stack.append([ny, nx, [li[i][j][0][0] // 2, li[i][j][0][1] % 2 + 1]])
                elif nx == 0 or nx == N - 1:
                    if li[i][j][0][1] == 3:
                        # li[ny][nx].append([li[i][j][0][0] // 2, 4])
                        stack.append([ny, nx, [li[i][j][0][0] // 2, 4]])
                    else:
                        # li[ny][nx].append([li[i][j][0][0] // 2, 3])
                        stack.append([ny, nx, [li[i][j][0][0] // 2, 3]])
                else:
                    # li[ny][nx].append([li[i][j][0][0], li[i][j][0][1]])
                    stack.append([ny, nx, [li[i][j][0][0], li[i][j][0][1]]])
                li[i][j].pop()
    while stack:
        stack_ = stack.pop()
        li[stack_[0]][stack_[1]].append([stack_[2][0], stack_[2]][1])
    return


T = int(input())

for TC in range(1, T + 1):
    N, M, K = map(int, input().split())

    li = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        t_li = list(map(int, input().split()))
        li[t_li[0]][t_li[1]].append([t_li[2], t_li[3]])
    for i in range(M):
        play()
    result = 0

    for i in range(N):
        for j in range(N):
            if li[i][j]:
                for idx in range(len(li[i][j])):
                    result += li[i][j][idx][0]

    print('#%d %d' % (TC, result))
