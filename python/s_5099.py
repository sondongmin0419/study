import sys
sys.stdin = open("input_3.txt", "r")


T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())

    li = list(map(int, input().split()))
    li_li = [[0] * 2 for _ in range(M)]
    for i in range(M):
        li_li[i][0] = li[i]
        li_li[i][1] = i+1
    stack = []
    while True:
        while True:
            if len(stack) < N:
                if li_li:
                    stack.append(li_li.pop(0))
                else:
                    break
            if len(stack) == N:
                break
        if len(stack) == 1:
            break
        p = stack.pop(0)
        p[0] = p[0] // 2
        if p[0] != 0:
            stack.append(p)
    print('#%d %d' % (TC, stack[0][1]))