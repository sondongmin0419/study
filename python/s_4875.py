import sys
sys.stdin = open("input_3.txt", "r")


def play(y,x):
    global result
    li[y][x] = 1
    if y-1 >=0:
        if li[y-1][x] == '0':
            stack.append((y-1,x))
            stack.append((y-1,x))
        elif li[y-1][x] == '3':
            result = 1
            return
    if x+1 <N:
        if li[y][x+1] == '0':
            stack.append((y, x+1))
            stack.append((y, x+1))

        elif li[y][x+1] == '3':
            result = 1
            return
    if y+1 <N:
        if li[y + 1][x] == '0':
            stack.append((y + 1, x))
            stack.append((y + 1, x))

        elif li[y+1][x] == '3':
            result = 1
            return
    if x-1 >=0:
        if li[y][x-1] == '0':
            stack.append((y,x-1))
            stack.append((y,x-1))

        elif li[y][x-1] == '3':
            result = 1
    return


T = int(input())

for TC in range(1, T+1):
    stack = []
    N = int(input())
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