def play(n):
    cnt = 0
    for i in range(1, N+1):
        if li_[n][i] == 1:
            v[n] = 1
            v[i] = 1
            cnt += 1
            li_[i][n] = 0
            li_[n][i] = 0
            play(i)
    if cnt == 0:
        return 0
    else:
        return 1



T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input(). split())
    li = list(map(int, input().split()))
    li_ = [[0] * (N+1) for _ in range(N+1)]
    v = [0]*(N+1)
    v[0] = 1
    for _ in range(M):
        a = li.pop(0)
        b = li.pop(0)
        li_[a][b] = 1
        li_[b][a] = 1
    result = 0
    for i in range(1, N+1):
        result += play(i)
    result += v.count(0)
    print('#%d %d' % (TC, result))