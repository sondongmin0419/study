import sys

sys.stdin = open("input_4.txt", "r")


def play(len_v):
    global result
    global cnt
    cnt += 1
    for _ in range(len_v):
        s_v = stack.pop(0)
        for i in range(1, V+1):
            if li_e[s_v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                if i == G:
                    result = 1
                    return
                stack.append(i)
    return


T = int(input())

for TC in range(1, T + 1):
    V, E = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(E)]
    li_e = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(len(li)):
        li_e[li[i][0]][li[i][1]] = 1
        li_e[li[i][1]][li[i][0]] = 1

    S, G = map(int, input().split())
    stack = []
    stack.append(S)
    visited = [0] * (V + 1)
    visited[S] = 1
    result = 0
    cnt = 0
    while result == 0:
        if len(stack) == 0:
            break
        play(len(stack))

    if result == 1:
        print('#%d %d' % (TC, cnt))
    else:
        print('#%d %d' % (TC, 0))
