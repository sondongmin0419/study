import sys
sys.stdin = open("input_4.txt", "r")


def play(s_v):
    global result
    global cnt
    global min_cnt
    if cnt > min_cnt:
        cnt -= 1
        return 51
    visited[s_v] = 1
    for i in range(1,V+1):
        if li_e[s_v][i] == 1 and visited[i] == 0:
            cnt += 1
            if i == G:
                if min_cnt > cnt:
                    min_cnt = cnt
                result = 1
            
                return 51
            stack.append(s_v)
            return i


    cnt -= 1
    return 51

T = int(input())

for TC in range(1, T+1):
    V, E = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(E)]
    li_e = [[0] * (V+1) for _ in range(V+1)]
    for i in range(len(li)):
        li_e[li[i][0]][li[i][1]] = 1
        li_e[li[i][1]][li[i][0]] = 1

    S, G = map(int, input().split())
    stack = []
    visited = [0] * (V+1)
    result = 0
    cnt = 0
    min_cnt = 50*50
    while True:
        n_s = play(S)
        S = n_s
        if S == 51:
            if stack:
                S = stack.pop()
            else:
                break
    if result == 1:
        print('#%d %d' % (TC, min_cnt))
    else:
        print('#%d %d' % (TC, 0))
