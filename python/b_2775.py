T = int(input())

for TC in range(1, T+1):
    k = int(input())
    n = int(input())
    li = [[0] * (n+1) for _ in range(k+1)]

    for i in range(1, n+1):
        li[0][i] = i
    for i in range(1, k+1):
        for j in range(1, n+1):
            sum = 0
            for m in range(1, j+1):
                sum += li[i-1][m]
            li[i][j] = sum

    print(li[k][n])

