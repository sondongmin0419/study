N = 6


def play():
    if len(v) == 15:
        sum_v = 0
        for q in range(15):
            sum_v += int(v[q])
        if sum_v != (li_1[0][0] + li_1[1][0] + li_1[2][0] + li_1[3][0] + li_1[4][0]):
            v.pop()
            return
    if len(v) == 15 and " ".join(v) not in result:
        result.add(" ".join(v))
        # print(result)
        v.pop()
        return 0
    if len(v) == 5:
        sum_v = 0
        for q in range(5):
            sum_v += int(v[q])

        if sum_v != li_1[0][0]:
            v.pop()
            return 0
    if len(v) == 9:
        sum_v = 0
        for q in range(9):
            sum_v += int(v[q])
        if sum_v != (li_1[0][0]+li_1[1][0]):
            v.pop()
            return
    if len(v) == 12:
        sum_v = 0
        for q in range(12):
            sum_v += int(v[q])
        if sum_v != (li_1[0][0] + li_1[1][0] + li_1[2][0]):
            v.pop()
            return
    if len(v) == 14:
        sum_v = 0
        for q in range(14):
            sum_v += int(v[q])
        if sum_v != (li_1[0][0] + li_1[1][0] + li_1[2][0] + li_1[3][0]):
            v.pop()
            return
    for k in range(3):
        if li_c[k] == 1:
            v.append('1')
            play()
        elif li_c[k] == 0:
            v.append('0')
            play()
        elif li_c[k] == -1:
            v.append('-1')
            play()
    if len(v)>0:
        v.pop()
    else:
        return 0



#  ab ac ad ae af ba bc bd be bf  ca cb cd ce cf  da db dc de df  ea eb ec ed ef
#  1  1  1  1  1 / 0 1  1  1  0 /
#
for TC in range(4):

    li_c = [1, 0, -1]
    v = []
    result = set()
    li = list(map(int, input().split()))

    li_1 = [[0]*3 for _ in range(6)]
    for i in range(6):
        for j in range(3):
            li_1[i][j] = li[i*3+j]

    #승 무 패
    play()
    print(result)
