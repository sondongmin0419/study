import sys
sys.stdin = open("input_1248.txt", "r")


def play(v1_, v2_):
    while True:
        v1_ = li_2[v1_]
        v2_ = li_2[v2_]
        if v1_ not in stack:
            if v1_ != 0:
                stack.append(v1_)
        else:
            return v1_
        if v2_ not in stack:
            if v2_ != 0:
                stack.append(v2_)
        else:
            return v2_


def s_count(r):
    global cnt
    for i in range(2):
        if li[r][i] != 0:
            cnt += 1
            s_count(li[r][i])

T = int(input())

for TC in range(1, T+1):
    V, E, v1, v2 = map(int, input().split())
    li = [[0] * 2 for _ in range(V+1)]
    li_2 = [0] * (V+1)
    in_li = list(map(int, input().split()))
    stack = []
    c_stack = []
    
    for i in range(E):
        if li[in_li[i*2]][0] == 0:
            li[in_li[i * 2]][0] = in_li[i*2+1]
        else:
            li[in_li[i * 2]][1] = in_li[i*2+1]
        li_2[in_li[i*2+1]] = in_li[i*2]

    result = play(v1, v2)
    cnt = 1
    s_count(result)
    print('#%d %d %d' % (TC, result, cnt))

