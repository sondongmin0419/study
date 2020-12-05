dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]


def play(y, x, n):
    ny = y + dy[n]
    nx = x + dx[n]
    if n == 3 and ny == i and nx == j:
        s_ = stack[:]
        result.append(s_)
        return
    elif n == 4:
        return
    if 0 <= ny < N and 0 <= nx < N and li[ny][nx] not in stack:
        for idx in range(n,4):
            stack.append(li[ny][nx])
            play(ny, nx, idx)
            stack.pop()

    return


T = int(input())

for TC in range(1, T + 1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]

    stack = []
    result = []
    for i in range(N):
        for j in range(N):
            stack.append(li[i][j])
            play(i, j, 0)
            stack.pop()
    max_food = 0
    for i in range(len(result)):
        if len(result[i]) > max_food:
            max_food = len(result[i])
    print('#%d' %TC, end=' ')
    if max_food > 0:
        print(max_food)
    else:
        print('-1')
