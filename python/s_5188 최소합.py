def play(i, j):
    global sum_
    global min_sum
    if i >= N or j >= N:
        return
    sum_ += li[i][j]
    if i == N-1 and j == N-1:
        if sum_ < min_sum:
            min_sum = sum_
            sum_ -= li[i][j]
            return
    if sum_ > min_sum:
        sum_ -= li[i][j]
        return
    play(i+1, j)
    play(i, j + 1)
    sum_ -= li[i][j]


T = int(input())

for TC in range(1, T+1):
    N = int(input())

    li = []
    for _ in range(N):
        li.append(list(map(int, input().split())))

    sum_ = 0
    min_sum = N*N*10
    play(0, 0)
    print('#%d %d' %(TC, min_sum))