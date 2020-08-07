T = int(input())

for tc in range(T):
    n = int(input())

    a = []
    b = []
    for i in range(n):
        mini = []
        for j in range(n):
            mini.append(0)
        a.append(mini)

    cnt = 0
    max_n = n*n
    i = 0
    j = 0
    k = 0
    while cnt < max_n:

        while cnt < max_n:   #00 01 02 03
            cnt += 1
            a[i][j] = cnt
            j += 1
            if j == n-k:
                j -= 1
                i += 1
                break
        while cnt < max_n:
            cnt += 1
            a[i][j] = cnt
            i += 1
            if i == n-k:
                i -= 1
                j -= 1
                break
        while cnt < max_n:
            cnt += 1
            a[i][j] = cnt
            j -= 1
            if j == -1+k:
                j += 1
                i -= 1
                break
        while cnt < max_n:
            cnt += 1
            a[i][j] = cnt
            i -= 1
            if i == 0 + k:
                i += 1
                j += 1
                break
        k += 1
    print(f'#{tc+1}')
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
