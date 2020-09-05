def play(li_test):
    for k in range(3):
        if li_test[0] != 0:
            v.append(1)
            li_test[0] -= 1
            play(li_test)
        elif li_test[1] != 0:
            v.append(0)
            li_test[1] -= 1
            play(li_test)
        elif li_test[2] != 0:
            v.append(-1)
            li_test[2] -= 1
            play(li_test)
        pass


for TC in range(4):
    li = list(map(int, input().split()))

    li_1 = [[0]*3 for _ in range(6)]
    for i in range(6):
        for j in range(3):
            li_1[i][j] = li[i*3+j]

    print(li_1)
    v = []
    # for i in range(li_1[0][0]):

    # play(li_1[0])
