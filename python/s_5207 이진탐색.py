T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())

    li_n = list(map(int, input().split()))
    li_m = list(map(int, input().split()))
    li_n.sort()
    cnt = 0
    for i in range(M):
        l = 0
        r = N-1
        ch = 0
        while l <= r:

            m = (r+l)//2
            if li_n[m] == li_m[i]:
                cnt += 1
                break
            elif li_n[m] < li_m[i]:
                if ch == 1:
                    break
                ch = 1
                l = m+1
            else:
                if ch == -1:
                    break
                ch = -1
                r = m-1


    print('#%d %d' %(TC, cnt))

