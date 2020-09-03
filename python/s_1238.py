import sys
sys.stdin = open("input_5.txt", "r")


def play(len_v):
    global max_result
    global cnt
    max = 0
    cnt += 1

    for _ in range(len_v):
        s_v = stack.pop(0)
        for i in range(1, max_n + 1):
            if li_e[s_v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stack.append(i)
                if i > max:
                    max = i
    if max == 0:
        return
    else:
        max_result = max
    return


for TC in range(1, 11):

    N, S = map(int, input().split())
    li = list(map(int, input().split()))

    max_n = max(li)

    li_e = [[0] * (max_n+1) for _ in range(max_n+1)]
    visited = [0] * (max_n+1)
    stack = []
    max_result = 0
    cnt = 0
    for i in range(N//2):
        s = li.pop(0)
        t = li.pop(0)
        li_e[s][t] = 1
    stack.append(S)
    result = 0

    while True:
        if len(stack) == 0:
            break
        play(len(stack))
    print('#%d %d' % (TC, max_result))
