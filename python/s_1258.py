T = int(input())

for TC in range(1, T+1):
    n = int(input())

    li = [[0] * n for _ in range(n)]
    for i in range(n):
        li[i] = list(map(int, input().split()))
    bool_li = [[False] * n for _ in range(n)]
    result = []
    start_r = 0
    end_r = -1
    end_c = 0
    for i in range(n):
        r_cnt = 0
        c_cnt = 1
        for j in range(n):
            if bool_li[i][j] != 'True':
                if li[i][j] != 0 and j != n-1:
                    r_cnt += 1
                    bool_li[i][j] = 'True'
                    if r_cnt == 1:
                        start_r = j
                    if li[i][j+1] == 0:
                        end_r = j
                elif li[i][j] != 0 and j == n-1:
                    r_cnt += 1
                    end_r = j
                if end_r > -1:
                    for m in range(1, n-i):
                        if li[i+m][j] != 0 and i+m != n-1:
                            c_cnt += 1
                            bool_li[i+m][j] = 'True'
                            if li[i+m+1][j] == 0:
                                end_c = i+m
                        elif li[i+m][j] != 0 and i+m == n-1:
                            c_cnt += 1
                            end_c = i+m
                            break
                        elif li[i+m][j] == 0:
                            end_c = i+m
                            break
                        if end_c > 0:
                            break
                    result.append([c_cnt, r_cnt])

                    for c in range(i, i+c_cnt):
                        for r in range(start_r, end_r+1):
                            bool_li[c][r] = 'True'
                    c_cnt = 1
                    r_cnt = 0
                    end_c = 0
                    end_r = -1
    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            if result[i][0]*result[i][1] > result[j][0]*result[j][1]:
                result[i], result[j] = result[j], result[i]
            elif result[i][0]*result[i][1] == result[j][0]*result[j][1]:
                if result[i][0] > result[j][0]:
                    result[i], result[j] = result[j], result[i]
    print(f'#{TC} {len(result)} ', end='')
    for i in range(len(result)):
        print(f'{result[i][0]} {result[i][1]}', end=' ')
    print()
