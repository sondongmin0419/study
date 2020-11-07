T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    li_w = list(map(int, input().split()))
    li_t = list(map(int, input().split()))

    li_w.sort(reverse=True)
    li_t.sort(reverse=True)
    sum_w = 0
    while li_t and li_w:
        w = li_w.pop(0)
        if li_t[0] >= w:
            sum_w += w
            li_t.pop(0)

    print('#%d %d' %(TC, sum_w))
