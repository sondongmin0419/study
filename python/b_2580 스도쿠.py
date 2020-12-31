import copy


def d_2580(n):
    y, x = temp_arr[n]
    cnt = 0
    for i in range(9):
        if (y, i) not in temp_arr and arr[y][i] in arr_2[y][x]:
            cnt += 1
            arr_2[y][x].remove(arr[y][i])
        if (i, x) not in temp_arr and arr[i][x] in arr_2[y][x]:
            cnt += 1
            arr_2[y][x].remove(arr[i][x])
    s_x = x // 3 *3
    s_y = y // 3 *3
    for i in range(s_y, s_y + 3):
        for j in range(s_x, s_x + 3):
            if (i, j) not in temp_arr and arr[i][j] in arr_2[y][x]:
                cnt += 1
                arr_2[y][x].remove(arr[i][j])
    return cnt

arr_2 = [[[] for _ in range(9)] for _ in range(9)]

arr = [list(map(int, input().split())) for _ in range(9)]
nums = [0] * 10
temp_arr = []
for i in range(9):
    for j in range(9):
        nums[arr[i][j]] += 1
        if arr[i][j] == 0:
            temp_arr.append((i, j))
            for k in range(1, 10):
                arr_2[i][j].append(k)

while temp_arr:
    cnt = 0
    for i in range(len(temp_arr)):
        cnt = d_2580(i)
    if cnt == 0:
        break
    k = 0
    while k<len(temp_arr):
        i,j = temp_arr[k]
        if len(arr_2[i][j]) == 1:
            arr[i][j] = arr_2[i][j].pop()
            temp_arr.remove((i,j))
            continue
        k+=1


for i in range(len(temp_arr[0])):
    n_temp_arr = copy.deepcopy(temp_arr)
    n_arr_2 = copy.deepcopy(arr_2)
    n_arr = copy.deepcopy(arr)



for i in range(9):
    print(*arr[i])
