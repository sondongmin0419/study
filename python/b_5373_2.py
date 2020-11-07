def rot(test_li, r):
    li__ = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            li__[i][j] = test_li[i][j]

    if r == '+':
        test_li[0][0:3] = li__[2:0][0]
        test_li[0][0] = li__[2][0]   # * * *
        test_li[0][1] = li__[1][0]   # * * *
        test_li[0][2] = li__[0][0]   # * * *
        test_li[1][0] = li__[2][1]
        test_li[1][1] = li__[1][1]
        test_li[1][2] = li__[0][1]
        test_li[2][0] = li__[2][2]
        test_li[2][1] = li__[1][2]
        test_li[2][2] = li__[0][2]
    else:
        test_li[0][0] = li__[0][2]   # * * *
        test_li[0][1] = li__[1][2]   # * * *
        test_li[0][2] = li__[2][2]   # * * *
        test_li[1][0] = li__[0][1]
        test_li[1][1] = li__[1][1]
        test_li[1][2] = li__[2][1]
        test_li[2][0] = li__[0][0]
        test_li[2][1] = li__[1][0]
        test_li[2][2] = li__[2][0]


def play(test, li_):
    area = test[0]
    r = test[1]
    if area == 'U':
        if r == '+':
            li_[1][0][0], li_[1][0][1], li_[1][0][2], li_[2][0][0], li_[2][0][1], li_[2][0][2], li_[3][0][0], li_[3][0][
                1], li_[3][0][2], li_[4][0][0], li_[4][0][1], li_[4][0][2] = li_[2][0][0], li_[2][0][1], li_[2][0][2], \
                                                                             li_[4][0][0], li_[4][0][1], li_[4][0][2], \
                                                                             li_[1][0][2], li_[1][0][1], li_[1][0][0], \
                                                                             li_[3][0][2], li_[3][0][1], li_[3][0][0]
        else:
            li_[1][0][0], li_[1][0][1], li_[1][0][2], li_[2][0][0], li_[2][0][1], li_[2][0][2], li_[3][0][0], li_[3][0][
                1], li_[3][0][2], li_[4][0][0], li_[4][0][1], li_[4][0][2] = li_[3][0][2], li_[3][0][1], li_[3][0][1], \
                                                                             li_[1][0][0], li_[1][0][1], li_[1][0][2], \
                                                                             li_[4][0][2], li_[4][0][1], li_[4][0][0], \
                                                                             li_[2][0][0], li_[2][0][1], li_[2][0][2]
        rot(li_[0], r)

    elif area == 'D':
        if r == '+':
            r = '-'
        else:
            r = '+'
        if r == '+':
            li_[1][2][0], li_[1][2][1], li_[1][2][2], li_[2][2][0], li_[2][2][1], li_[2][2][2], li_[3][2][0], li_[3][2][
                1], li_[3][2][2], li_[4][2][0], li_[4][2][1], li_[4][2][2] = li_[2][2][0], li_[2][2][1], li_[2][2][2], \
                                                                             li_[4][2][0], li_[4][2][1], li_[4][2][2], \
                                                                             li_[1][2][2], li_[1][2][1], li_[1][2][0], \
                                                                             li_[3][2][2], li_[3][2][1], li_[3][2][0]
        else:
            li_[1][2][0], li_[1][2][1], li_[1][2][2], li_[2][2][0], li_[2][2][1], li_[2][2][2], li_[3][2][0], li_[3][2][
                1], li_[3][2][2], li_[4][2][0], li_[4][2][1], li_[4][2][2] = li_[3][2][2], li_[3][2][1], li_[3][2][0], \
                                                                             li_[1][2][0], li_[1][2][1], li_[1][2][2], \
                                                                             li_[4][2][2], li_[4][2][1], li_[4][2][0], \
                                                                             li_[2][2][0], li_[2][2][1], li_[2][2][2]
        rot(li_[5], r)
    elif area == 'L':
        if r == '+':
            li_[0][0][0], li_[0][1][0], li_[0][2][0], li_[2][0][0], li_[2][1][0], li_[2][2][0], li_[5][0][0], li_[5][1][
                0], li_[5][2][0], li_[3][0][0], li_[3][1][0], li_[3][2][0] = li_[3][2][0], li_[3][1][0], li_[3][0][0], \
                                                                             li_[0][0][0], li_[0][1][0], li_[0][2][0], \
                                                                             li_[2][2][0], li_[2][1][0], li_[2][0][0], \
                                                                             li_[5][0][0], li_[5][1][0], li_[5][2][0]
        else:
            li_[0][0][0], li_[0][1][0], li_[0][2][0], li_[2][0][0], li_[2][1][0], li_[2][2][0], li_[5][0][0], li_[5][1][
                0], li_[5][2][0], li_[3][0][0], li_[3][1][0], li_[3][2][0] = li_[2][0][0], li_[2][1][0], li_[2][2][0], \
                                                                             li_[5][2][0], li_[5][1][0], li_[5][0][0], \
                                                                             li_[3][0][0], li_[3][1][0], li_[3][2][0], \
                                                                             li_[0][2][0], li_[0][1][0], li_[0][0][0]

        rot(li_[1], r)

    elif area == 'R':
        if r == '+':
            li_[0][0][2], li_[0][1][2], li_[0][2][2], li_[2][0][2], li_[2][1][2], li_[2][2][2], li_[5][0][2], li_[5][1][
                2], li_[5][2][2], li_[3][0][2], li_[3][1][2], li_[3][2][2] = li_[2][0][2], li_[2][1][2], li_[2][2][2], \
                                                                             li_[5][2][2], li_[5][1][2], li_[5][0][2], \
                                                                             li_[3][0][2], li_[3][1][2], li_[3][2][2], \
                                                                             li_[0][2][2], li_[0][1][2], li_[0][0][2]
        else:
            li_[0][0][2], li_[0][1][2], li_[0][2][2], li_[2][0][2], li_[2][1][2], li_[2][2][2], li_[5][0][2], li_[5][1][
                2], li_[5][2][2], li_[3][0][2], li_[3][1][2], li_[3][2][2] = li_[3][2][2], li_[3][1][2], li_[3][0][2], \
                                                                             li_[0][0][2], li_[0][1][2], li_[0][2][2], \
                                                                             li_[2][2][2], li_[2][1][2], li_[2][0][2], \
                                                                             li_[5][0][2], li_[5][1][2], li_[5][2][2]

        rot(li_[4], r)

    elif area == 'F':
        if r == '+':
            li_[0][2][0], li_[0][2][1], li_[0][2][2], li_[4][0][0], li_[4][1][0], li_[4][2][0], li_[5][2][0], li_[5][2][
                1], li_[5][2][2], li_[1][0][2], li_[1][1][2], li_[1][2][2] = li_[1][2][2], li_[1][1][2], li_[1][0][2], \
                                                                             li_[0][2][0], li_[0][2][1], li_[0][2][2], \
                                                                             li_[4][2][0], li_[4][1][0], li_[4][0][0], \
                                                                             li_[5][2][0], li_[5][2][1], li_[5][2][2]
        else:
            li_[0][2][0], li_[0][2][1], li_[0][2][2], li_[4][0][0], li_[4][1][0], li_[4][2][0], li_[5][2][0], li_[5][2][
                1], li_[5][2][2], li_[1][0][2], li_[1][1][2], li_[1][2][2] = li_[4][0][0], li_[4][1][0], li_[4][2][0], \
                                                                             li_[5][2][2], li_[5][2][1], li_[5][2][0], \
                                                                             li_[1][0][2], li_[1][1][2], li_[1][2][2], \
                                                                             li_[0][2][2], li_[0][2][1], li_[0][2][0]

        rot(li_[2], r)

    else:
        if r == '+':
            r = '-'
        else:
            r = '+'
        if r == '+':
            li_[0][0][0], li_[0][0][1], li_[0][0][2], li_[4][0][2], li_[4][1][2], li_[4][2][2], li_[5][0][0], li_[5][0][
                1], li_[5][0][2], li_[1][0][0], li_[1][1][0], li_[1][2][0] = li_[1][2][0], li_[1][1][0], li_[1][0][0], \
                                                                             li_[0][0][0], li_[0][0][1], li_[0][0][2], \
                                                                             li_[4][2][2], li_[4][1][2], li_[4][0][2], \
                                                                             li_[5][0][0], li_[5][0][1], li_[5][0][2]
        else:
            li_[0][0][0], li_[0][0][1], li_[0][0][2], li_[4][0][2], li_[4][1][2], li_[4][2][2], li_[5][0][0], li_[5][0][
                1], li_[5][0][2], li_[1][0][0], li_[1][1][0], li_[1][2][0] = li_[4][0][2], li_[4][1][2], li_[4][2][2], \
                                                                             li_[5][0][2], li_[5][0][1], li_[5][0][0], \
                                                                             li_[1][0][0], li_[1][1][0], li_[1][2][0], \
                                                                             li_[0][0][2], li_[0][0][1], li_[0][0][0]
        rot(li_[3], r)


T = int(input())




for TC in range(1, T+1):
    li_ = []

    li_.append([['w', 'w', 'w'] for _ in range(3)])  # 위 0
    li_.append([['g', 'g', 'g'] for _ in range(3)])  # 왼 1
    li_.append([['r', 'r', 'r'] for _ in range(3)])  # 앞 2
    li_.append([['o', 'o', 'o'] for _ in range(3)])  # 뒤 3
    li_.append([['b', 'b', 'b'] for _ in range(3)])  # 오 4
    li_.append([['y', 'y', 'y'] for _ in range(3)])  # 아래 5
    n = int(input())

    li = list(map(str, input().split()))
    for i in range(n):
        play(li[i], li_)
        # for k in range(6):
        #     print(li_[k])
        # print()
    for i in range(3):
        for j in range(3):
            print(li_[0][i][j], end='')
        print()