T = int(input())

for TC in range(1,T+1):
    N, M = map(int, input().split())

    li = [[0] for _ in range(N)]

    min_w = N*M
    for i in range(N):
        li[i] = list(input())

    for i in range(N-2):
        for j in range(i, N-1):
            s1 = 0
            s2 = 0
            s3 = 0
            total = 0
            for a in range(i+1):
                s1 += M - li[a].count('W')
            for b in range(i+1,j+1):
                s2 += M - li[b].count('B')
            for k in range(j+1, N):
                s3 += M - li[k].count('R')
            total = s1 + s2 + s3
            if total < min_w:
                min_w = total
    print(f'#{TC} {min_w}')