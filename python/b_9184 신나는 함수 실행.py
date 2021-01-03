arr = [[[0 for _ in range(22)] for _ in range(22)] for _ in range(22)]
arr[0][0][0] = 1
for A in range(21):
    for B in range(21):
        for C in range(21):
            if A * B * C == 0:
                arr[A][B][C] = 1

            cnt = 0
            if A < B < C + 1:
                arr[A][B][C + 1] += arr[A][B][C]
            if A < B + 1 < C + 1:
                arr[A][B + 1][C + 1] += arr[A][B][C]
            if A < B + 1 < C:
                arr[A][B + 1][C] -= arr[A][B][C]

            if (A + 1) < B < C:
                pass
            else:
                arr[A + 1][B][C] += arr[A][B][C]
            if (A + 1) < (B + 1) < C:
                pass
            else:
                arr[A + 1][B + 1][C] += arr[A][B][C]
            if (A + 1) < B < (C + 1):
                pass
            else:
                arr[A + 1][B][C + 1] += arr[A][B][C]
            if (A + 1) < (B + 1) < (C + 1):
                pass
            else:
                arr[A + 1][B + 1][C + 1] -= arr[A][B][C]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w(%d, %d, %d) = ' % (a, b, c), end='')
    if a <= 0 or b <= 0 or c <= 0:
        print(1)
    elif a > 20 or b > 20 or c > 20:
        print(arr[20][20][20])
    else:
        print(arr[a][b][c])
