def play(n, x, y):
    global d
    global min_d

    if n == N:
        d += abs(home_x-x) + abs(home_y-y)
        if d < min_d:
            min_d = d
        d -= abs(home_x-x) + abs(home_y-y)
        return
    if d > min_d:
        return


    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            d += abs(li[i*2] - x) + abs(li[i*2+1] - y)

            play(n+1, li[i*2], li[i*2+1])
            d -= abs(li[i*2] - x) + abs(li[i*2+1] - y)
            visited[i] = 0


T = int(input())

for TC in range(1, T+1):
    N = int(input())

    li = list(map(int, input().split()))
    
    visited = [0] * N
    com_x = li.pop(0)
    com_y = li.pop(0)
    home_x = li.pop(0)
    home_y = li.pop(0)

    min_d = 100 * 100 * 10
    d = 0
    play(0, com_x, com_y)
    print('#%d %d' %(TC, min_d))