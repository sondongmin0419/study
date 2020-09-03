N = 6


def play():
    global result
    if result == 1:
        return
    if len(v) == 5:
        if li_2[0] != li_1[0]:
            return
    elif len(v) == 9:
        if li_2[1] != li_1[1]:
            return
    elif len(v) == 12:
        if li_2[2] != li_1[2]:
            return
    elif len(v) == 14:
        if li_2[3] != li_1[3]:
            return
    elif len(v) == 15:
        if li_2[4] != li_1[4]:
            return
        else:
            if li_2[5] == li_1[5]:
                result = 1
                return
            return
    for k in range(3):
        if li_c[k] == 1:
            v.append('1')
        elif li_c[k] == 0:
            v.append('0')
        elif li_c[k] == -1:
            v.append('-1')
        v_i = len(v)

        if len(v) <= 5:
            i = 0
        elif len(v) <= 9:
            i = 1
        elif len(v) <= 12:
            i = 2
        elif len(v) <= 14:
            i = 3
        else:
            i = 4
        j = (v_i - 1+i) % 5
        if i == 0:
            j += 1
        if i == 3:
            j += 1
        if i == 4:
            j = 1
        if li_c[k] == 1:
            li_2[i][0] += 1
            li_2[j+i][2] += 1
            play()
            li_2[i][0] -= 1
            li_2[j + i][2] -= 1
        elif li_c[k] == 0:
            li_2[i][1] += 1
            li_2[j+i][1] += 1
            play()
            li_2[i][1] -= 1
            li_2[j + i][1] -= 1
        elif li_c[k] == -1:
            li_2[i][2] += 1
            li_2[j+i][0] += 1
            play()
            li_2[i][2] -= 1
            li_2[j + i][0] -= 1
        v.pop()
    else:
        return 0



#  ab ac ad ae af  bc bd be bf   cd ce cf  de df  ef
#  1  1  1  1  1 / 0 1  1  1  0 /
#
for TC in range(4):

    li_c = [1, 0, -1]
    v = []
    result = 0
    li = list(map(int, input().split()))
    li_2 = [[0]*3 for _ in range(6)]
    li_1 = [[0]*3 for _ in range(6)]
    for i in range(6):
        for j in range(3):
            li_1[i][j] = li[i*3+j]

    #승 무 패
    play()
    print(result)
