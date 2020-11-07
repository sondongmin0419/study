def Dijkstra(s, A, D):
    U = {s}

    for i in range(N+1):
        if li[s][i] >0:
            A[i] = 1
            D[i] = li[s][i]

    while N not in U:
        W = 1000
        idx = 0
        for j in range(N+1):
            if j not in U and D[j] < W:
                W = D[j]
                idx = j

        U.add(idx)

        for i in range(N+1):
            D[i] = min(D[i], D[idx]+li[idx][i])




T = int(input())

for TC in range(1, T + 1):
    N, E = map(int, input().split())
    li = [[1000] * (N+1) for _ in range(N+1)]
    dic = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        li[s][e] = w
    for i in range(N+1):
        li[i][i] = 0
    A = [0] * (N+1)
    D = [1000] * (N+1)


    Dijkstra(0, A, D)
    print('#%d %d' %(TC,D[N]))
