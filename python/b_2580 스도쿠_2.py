import sys


def d_2580(n):
    if n == len(temp_arr):
        for i in range(9):
            print(*arr[i])
        sys.exit()
    y, x = temp_arr[n]
    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if arr[y][i] in stack and i != x:
            stack.remove(arr[y][i])
        if arr[i][x] in stack and i != y:
            stack.remove(arr[i][x])

    s_x = x // 3 * 3
    s_y = y // 3 * 3
    for i in range(s_y, s_y + 3):
        for j in range(s_x, s_x + 3):
            if arr[i][j] in stack and i != y and j != x:
                stack.remove(arr[i][j])
    for k in range(len(stack)):
        arr[y][x] = stack[k]
        d_2580(n + 1)
        arr[y][x] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
nums = [0] * 10
temp_arr = []
for i in range(9):
    for j in range(9):
        nums[arr[i][j]] += 1
        if arr[i][j] == 0:
            temp_arr.append((i, j))

d_2580(0)
