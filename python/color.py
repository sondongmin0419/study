T = int(input())

for TC in range(1, T+1):
    n = int(input())
    li = [[[0, 0] for _ in range(10)] for __ in range(10)]
    # li = []
    # for _ in range(10):
    #     mini = []
    #     for __ in range(10):
    #         mini.append([0, 0])
    #     li.append(mini)
    for areas in range(n):
        area = list(map(int, input().split()))
        for y in range(area[0], area[2]+1):
            for x in range(area[1], area[3]+1):
                if area[4] == 1:
                    li[x][y][0] = 1
                else:
                    li[x][y][1] = 1
    cnt = 0
    for x in range(10):
        for y in range(10):
            if li[x][y][0] == li[x][y][1] == 1:
                cnt += 1
    print(f'#{TC} {cnt}')
