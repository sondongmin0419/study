def play_1():
    for i in range(N):
        if sum(li[i]) == 0:
            continue
        li_ = []
        j = 0
        while j < M:

            li__ = li[i][j:j+8]
            if li__ == [0,0,0,1,1,0,1,0]:
                li_.append(0)
            elif li__ == [0,0,1,1,0,0,1,0]:
                li_.append(1)
            elif li__ == [0,0,1,0,0,1,1,0]:
                li_.append(2)
            elif li__ == [0,1,1,1,1,0,1,0]:
                li_.append(3)
            elif li__ == [0,1,0,0,0,1,1,0]:
                li_.append(4)
            elif li__ == [0,1,1,0,0,0,1,0]:
                li_.append(5)
            elif li__ == [0,1,0,1,1,1,1,0]:
                li_.append(6)
            elif li__ == [0,1,1,1,0,1,1,0]:
                li_.append(7)
            elif li__ == [0,1,1,0,1,1,1,0]:
                li_.append(8)
            elif li__ == [0,0,0,1,0,1,1,0]:
                li_.append(9)
            else:
                j += 1
                continue
            if len(li_) == 8:
                break
            j += 7
        sum_code = (li_[0] + li_[2] + li_[4] + li_[6]) * 3 + (li_[1] + li_[3] + li_[5]) + li_[7]
        if sum_code % 10 == 0:
            return sum(li_)
        else:
            return 0


T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    li = []
    for _ in range(N):
        li.append(list(map(int, list(input()))))
    print('#%d %d' %(TC, play_1()))
