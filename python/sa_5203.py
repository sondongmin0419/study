def run_(li_):
    li_.sort()
    cnt = 1
    for i in range(1, len(li_)):
        if li_[i] - li_[i-1] == 1:
            cnt += 1
        elif li_[i] - li_[i-1] == 0:
            continue
        else:
            cnt = 1

        if cnt == 3:
            return True


def triplet(li_):
    li_.sort()
    cnt = 1
    for i in range(1, len(li_)):
        if li_[i] == li_[i-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt == 3:
            return True


T = int(input())

for TC in range(1, T+1):
    li = list(map(int, input().split()))

    li_1 = []
    li_2 = []

    li_1_result = 0
    li_2_result = 0
    for i in range(6):
        li_1.append(li.pop(0))
        li_2.append(li.pop(0))

        if run_(li_1) or triplet(li_1):
            li_1_result = 1
            break
        if run_(li_2) or triplet(li_2):
            li_2_result = 2
            break
        # if li_1_result + li_2_result > 0:
        #     break

    print('#%d %d' % (TC, li_1_result + li_2_result))


