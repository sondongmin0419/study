def play(n):
    global V
    global min_V

    if n == N:
        if V < min_V:
            min_V = V
        return
    if V > min_V:
        return


    for j in range(N):
        if li_product[j] == 0:
            li_product[j] = 1
            V += li[n][j]
            play(n+1)
            V -= li[n][j]
            li_product[j] = 0


T = int(input())

for TC in range(1, T+1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]
    li_product = [0] * N
    li_factory = [0] * N
    min_V = 99 * 15 * 15
    V = 0
    play(0)
    print('#%d %d' %(TC, min_V))