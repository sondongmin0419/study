def play():
    for i in range(1, N + 1):
        if li[1][i] == 1:
            stack.append(i)
            li[1][i] = 0
            li[i][1] = 0

    for j in range(len(stack)):
        for i in range(1, N + 1):
            if li[stack[j]][i] == 1 and i not in stack:
                stack.append(i)
                li[j][i] = 0
                li[i][j] = 0


T = int(input())

for TC in range(1, T + 1):
    N, M = map(int, input().split())
    li = [[0] * (N + 1) for _ in range(N + 1)]
    v = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        li[a][b] = 1
        li[b][a] = 1
    stack = []
    play()
    print('#%d %d' %(TC, len(stack)))
