T = int(input())

def play(ch_):
    num = ch_[0] - 1
    r = ch_[1]
    if num+1 < 4:
        if li[num+1][6] != li[num][2]:
            if r == 1:
                play_r([ch_[0]+1, -1])
            else:
                play_r([ch_[0]+1, 1])

    if num-1 >= 0:
        if li[num-1][2] != li[num][6]:
            if r == 1:
                play_l((ch_[0]-1, -1))
            else:
                play_l((ch_[0]-1, 1))
    if r != 1:
        li[num].append(li[num].pop(0))
    else:
        li[num].insert(0, li[num].pop())



def play_r(ch2_):
    num = ch2_[0] - 1
    r = ch2_[1]
    if num + 1 < 4:
        if li[num + 1][6] != li[num][2]:
            if r == 1:
                play_r([ch2_[0] + 1, -1])
            else:
                play_r([ch2_[0] + 1, 1])
    if r != 1:
        li[num].append(li[num].pop(0))
    else:
        li[num].insert(0, li[num].pop())


def play_l(ch2_):
    num = ch2_[0] - 1
    r = ch2_[1]
    if num-1 >= 0:
        if li[num-1][2] != li[num][6]:
            if r == 1:
                play_l((ch2_[0] - 1, -1))
            else:
                play_l((ch2_[0] - 1, 1))

    if r != 1:
        li[num].append(li[num].pop(0))
    else:
        li[num].insert(0, li[num].pop())

for TC in range(1, T+1):
    K = int(input())
    li = [list(map(int, input().split())) for _ in range(4)]
    change = []
    for i in range(K):
        change.append(list(map(int, input().split())))
    for ch in change:
        play(ch)

    result = 0
    for i in range(4):
        result += li[i][0] * 2**(i)
    print('#%d %d' % (TC, result))