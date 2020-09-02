import sys
sys.stdin = open("input_100.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def play(y, x):
    global result
    li[y][x] = 1
    for i in range(4):
        if 0 <= y+dr[i] < N and 0 <= x+dc[i] < N:
            if li[y+dr[i]][x+dc[i]] == '0':
                stack.append((y+dr[i], x+dc[i]))
                stack.append((y+dr[i], x+dc[i]))
            elif li[y+dr[i]][x+dc[i]] == '3':
                result = 1
                return


T = 10
for TC in range(1, T+1):
    stack = []
    tc = int(input())
    N = 100
    li = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if li[i][j] == '2':
                stack.append((i,j))
                stack.append((i,j))
                break
    result = 0

    while True:
        y, x = stack.pop()
        play(y,x)
        if result == 1 or len(stack) == 0:
            break

    print('#%d %d' % (TC,result))