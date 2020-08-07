T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    li = [0] * N
    for i in range(N):
        li[i] = list(map(int, input().split()))
    max_kill = 0
    total_kill = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            total_kill = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    total_kill += li[y][x]
            if max_kill < total_kill:
                max_kill = total_kill
    print(f'#{TC} {max_kill}')

