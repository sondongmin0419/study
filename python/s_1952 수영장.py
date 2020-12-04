T = int(input())


def third(test_li, i):
    global min_third
    li_ = test_li[:]
    if (li_[i] + li_[i + 1] + li_[i + 2]) > t:
        li_[i] = t
        li_[i + 2] = 0
        li_[i + 1] = 0
        i += 3
    else:
        i += 1

    if i > 11:
        if sum(li_) < min_third:
            min_third = sum(li_)
        return
    for k in range(i, 12):
        third(li_, k)


for TC in range(1, T + 1):
    d, m, t, y = map(int, input().split())
    li = list(map(int, input().split()))
    li.append(0)
    li.append(0)
    for i in range(12):
        if li[i] * d > m:
            li[i] = m
        else:
            li[i] = li[i] * d
    min_third = y
    for j in range(12):
        third(li, j)
    print('#%d %d' % (TC, min_third))
