import sys
sys.stdin = open("input_2.txt", "r")


def play(y, x):
    stack.append(str(li[y][x]))
    if len(stack) == 7:

        stack_str = ''.join(stack)
        if stack_str not in result:
            result.append(stack_str)
        return
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    for di in range(4):
        ny = y + dc[di]
        nx = x + dr[di]
        if 0 <= ny < 4 and 0 <= nx < 4:
            play(ny, nx)
            stack.pop()
    return


T = int(input())

for TC in range(1, T+1):

    stack = []
    result = []
    li = [list(map(int, input().split())) for _ in range(4)]

    for i in range(4):
        for j in range(4):
            stack = []
            play(i, j)

    print('#%d %d' % (TC, len(result)))