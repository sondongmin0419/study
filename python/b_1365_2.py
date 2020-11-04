import bisect


N = int(input())

li = list(map(int, input().split()))
li_ = [li[0]]

for i in range(1, N):
    if li[i] > li_[-1]:
        li_.append(li[i])
    else:
        it = bisect.bisect_left(li_, li[i])
        li_[it] = li[i]
print(N - len(li_))


