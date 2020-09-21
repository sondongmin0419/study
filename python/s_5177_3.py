T = int(input())

for TC in range(1, T+1):
    N = int(input())

    li = list(map(int, input().split()))
    h = [0]
    for i in range(N):
        h.append(li[i])
        num = len(h) - 1
        while num > 1:
            if h[num] < h[num//2]:
                h[num], h[num//2] = h[num//2], h[num]
            num = num // 2
    result = 0
    while N > 1:
        N = N//2
        result += h[N]
    print(h)
    print('#%d %d' % (TC,result))