T = int(input())

for TC in range(1, T+1):
    N, B = map(int, input().split())

    h = list(map(int, input().split()))

    stack = []
    min_h = 10000*20
    for i in range(1 << N):
        total = 0
        for j in range(N):
            if i & 1 << j:
                total += h[j]
                if total >= B:
                    if min_h > total:
                        min_h = total
                    break
    print('#%d %d' % (TC, min_h-B))