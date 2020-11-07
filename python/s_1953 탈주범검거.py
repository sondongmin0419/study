def BFS(r, c):
    dx, dy = dxdy(r, c)

    for i in range(len(dx)):
        nx = c + dx[i]
        ny = r + dy[i]
        if 0 <= nx < M and 0 <= ny < N and li[ny][nx] > 0 and (ny, nx) not in result and (r, c) in check(ny, nx):
            stack.append((ny, nx))
            result.add((ny, nx))


def check(r, c):
    dx, dy = dxdy(r, c)
    t_li = []
    for i in range(len(dx)):
        nx = c + dx[i]
        ny = r + dy[i]
        t_li.append((ny, nx))
    return t_li


def dxdy(r, c):
    dx = []
    dy = []
    if li[r][c] == 1:
        dx += [0, 1, 0, -1]
        dy += [1, 0, -1, 0]
    elif li[r][c] == 2:
        dx += [0, 0]
        dy += [1, -1]
    elif li[r][c] == 3:
        dx += [1, -1]
        dy += [0, 0]
    elif li[r][c] == 4:
        dx += [0, 1]
        dy += [-1, 0]
    elif li[r][c] == 5:
        dx += [1, 0]
        dy += [0, 1]
    elif li[r][c] == 6:
        dx += [0, -1]
        dy += [1, 0]
    elif li[r][c] == 7:
        dx += [0, -1]
        dy += [-1, 0]

    return dx, dy


T = int(input())

for TC in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    li_v = [[0] * N for _ in range(N)]
    result = {(R, C)}
    stack = [(R, C)]
    for _ in range(L - 1):

        s = len(stack)
        for _ in range(s):
            po = stack.pop(0)
            BFS(po[0], po[1])

    print('#%d %d' % (TC, len(result)))
