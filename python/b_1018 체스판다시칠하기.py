def b_1018(x, y):
    cnt = 0
    for r in range(8):
        for c in range(8):
            if (c + x + r + y) % 2 == 0:
                if arr[r + y][c + x] == 'W':
                    pass
                else:
                    cnt += 1
            else:
                if arr[r + y][c + x] == 'B':
                    pass
                else:
                    cnt += 1
    return cnt


N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
max_cnt = 0
low_cnt = 64
for i in range(M - 7):
    for j in range(N - 7):
        cnt = b_1018(i, j)
        if cnt < low_cnt:
            low_cnt = cnt
        if cnt > max_cnt:
            max_cnt = cnt

print(min(low_cnt,64-max_cnt))
