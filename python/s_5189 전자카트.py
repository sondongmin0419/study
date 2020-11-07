def play(n):
    global b_sum
    global b_min_sum
    visited[n] = 1

    if sum(visited) == N:
        b_sum += li[n][0]
        if b_sum < b_min_sum:
            b_min_sum = b_sum
        b_sum -= li[n][0]
        visited[n] = 0
        return

    if b_sum > b_min_sum:
        visited[n] = 0
        return

    for i in range(1, N):
        if visited[i] == 0:
            b_sum += li[n][i]
            play(i)
            b_sum -= li[n][i]
    visited[n] = 0

T = int(input())

for TC in range(1, T+1):
    N = int(input())

    li = []
    visited = [0] * N
    b_sum = 0
    b_min_sum = 100*10*10
    for _ in range(N):
        li.append(list(map(int, input().split())))

    play(1 - 1)

    print('#%d %d' %(TC, b_min_sum))