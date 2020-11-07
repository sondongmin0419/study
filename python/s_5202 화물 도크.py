T = int(input())

for TC in range(1, T+1):
    N = int(input())

    li_s = []
    for _ in range(N):
        li_s.append(list(map(int, input().split())))
    li_s.sort(key = lambda x: x[1])
    cnt = 0
    s = 0
    for time in li_s:
        if time[0] >= s:
            cnt += 1
            s = time[1]

    print('#%d %d' %(TC, cnt))