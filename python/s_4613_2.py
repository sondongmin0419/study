T = int(input())

for TC in range(1,T+1):
    N, M = map(int, input().split())

    li = [[0] for _ in range(N)]

    min_w = N*M
    for i in range(N):
        li[i] = list(input())

    W = [0]*N
    B = [0]*N
    R = [0]*N
    W[0] = M - li[0].count('W')
    B[0] = M - li[0].count('B')
    R[0] = M - li[0].count('R')

    for i in range(1, N):
        W[i] = W[i-1] + M - li[i].count('W')
        B[i] = B[i-1] + M - li[i].count('B')
        R[i] = R[i-1] + M - li[i].count('R')

    for i in range(N-2):
        for j in range(i, N-1):
            s1 = s2 = s3 = 0
            s1 = W[i]
            s2 = B[j]-B[i]
            s3 = R[N-1]-R[j]
            total = s1 + s2 + s3
            if total < min_w:
                min_w = total
    print(f'#{TC} {min_w}')