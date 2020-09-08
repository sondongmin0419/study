import sys
sys.stdin = open("input_1.txt", "r")


def play(n):
    for i in range(1, N+1):
        if li_li[n][i] == 1 and visited[i] == 0:
            visited[i] = 1
            stack.append(i)
    if stack:
        return play(stack.pop())
    else:
        return


T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(M)]
    li_li = [[0] * (N+1) for _ in range(N+1)]

    for i in range(len(li)):
        li_li[li[i][0]][li[i][1]] = 1
        li_li[li[i][1]][li[i][0]] = 1

    visited = [0] * (N+1)
    stack = []
    cnt = 0

    for i in range(1, N + 1):

        if visited[i] == 0:
            cnt += 1
            play(i)


    print('#%d %d' % (TC, cnt))

