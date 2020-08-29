N = 4


for TC in range(4):
    li = list(map(int, input().split()))

    li_1 = [[0]*3 for _ in range(6)]
    for i in range(6):
        for j in range(3):
            li_1[i][j] = li[i*3+j]

    result = True

    #조건1. 승 == 패 인지
    win = 0
    lose = 0
    same = 0
    same_cnt = 0
    same_team = 0
    max_same = 0
    win_5 = 0
    rose_5 = 0

    for i in range(6):
        win += li_1[i][0]
        same += li_1[i][1]
        lose += li_1[i][2]
        if li_1[i][0] + li_1[i][1] + li_1[i][2] != 5:     #조건2. 1줄에 5개씩
            result = False

        if li_1[i][1] != 0:
            max_same = max(li_1[i][1], max_same)
            same_team += 1

        if li_1[i][0] == 5:   # 5승이 2팀이면 안됨
            win_5 += 1
            if win_5 > 1:
                result = False
        if li_1[i][2] == 5:
            rose_5 += 1
            if rose_5 > 1:
                result = False
    if win != lose:
        result = False

    #조건3. 승+무/2 == 15
    if win + same//2 != 15:
        result = False

    #조건4. 무승부는 짝수 무승부 1팀이면 x
    if same % 2 == 1 or same_team == 1:
        result = False

    # 조건5. 무승부
    if max_same == 1:
        if same != same_team:
            result = False
    if same > 0:    # 1팀이 4번 팀 5개
        if same_team < max_same+1:
            result = False

    if result:
        print(1)
    else:
        print(0)

