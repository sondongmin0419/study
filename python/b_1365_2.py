# import bisect


def my_bisect(li_t, n):
    l = 0
    r = len(li_t) - 1
    while l <= r:
        m = (l + r) // 2
        if li_t[m - 1] < n < li_t[m]:
            return m
        elif li_t[m] > n:
            r = m - 1
        elif li_t[m] < n:
            l = m + 1

    return 0


N = int(input())

li = list(map(int, input().split()))
li_ = [li[0]]

for i in range(1, N):
    if li[i] > li_[-1]:
        li_.append(li[i])
    else:
        # it = bisect.bisect_left(li_, li[i])
        it = my_bisect(li_, li[i])
        li_[it] = li[i]

print(N - len(li_))
