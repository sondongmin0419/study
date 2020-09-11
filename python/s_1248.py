import sys
sys.stdin = open("input_1248.txt", "r")


def play(v1_, v2_):
    while True:
        for i in range(V,-1, -1):
            if li[i][v1_] == 1:
                v1_ = i
                if v1_ in stack:
                    return v1_
                stack.append(v1_)
                break
            if li[i][v2_] == 1:
                v2_ = i
                if v2_ in stack:
                    return v2_
                stack.append(v2_)
                break

def count_v(r):
    global cnt
    while True:
        for i in range(V+1):
            c_c = 0
            if li[r][i] == 1:
                cnt += 1
                c_c += 1
                c_stack.append(i)
                if c_c == 2:
                    break
        if c_stack:
            r = c_stack.pop()
        else:
            return


T = int(input())

for TC in range(1, T+1):
    V, E, v1, v2 = map(int, input().split())
    li = [[0] * (V+1) for _ in range(V+1)]
    in_li = list(map(int, input().split()))
    stack = []
    c_stack = []
    for i in range(E):
        li[in_li[i*2]][in_li[i*2+1]] = 1
    v1_ = v1
    v2_ = v2

    result = play(v1_, v2_)
    cnt = 1
    size = count_v(result)
    print('#%d %d %d' % (TC, result, cnt))