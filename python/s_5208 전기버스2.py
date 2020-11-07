def play(n):
    global cnt

    if n + li[n] >= li[0]:
        return
    cnt += 1
    max_n = 0
    next_i = 0
    for i in range(n+1, n+1+li[n]):
        next_n = i + li[i]
        if next_n > max_n:
            max_n = next_n
            next_i = i
    play(next_i)


T = int(input())

for TC in range(1, T+1):
    li = list(map(int, input().split()))
    cnt = 0
    play(1)
    print('#%d %d' %(TC, cnt))