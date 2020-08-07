T = int(input())

for TC in range(1, T+1):
    li = [0] * 9

    for j in range(9):
        li[j] = list(map(int, input().split()))
    cnt = 0

    for i in range(9):
        li_r = [0] * 9
        li_c = [0] * 9
        for num in li[i]:
            li_r[num-1] += 1   # 가로 비교
            if li_r[num-1] > 1:
                cnt += 1
                break
        if cnt > 0: break
        for j in range(9):     # 세로 비교
            li_c[li[j][i]-1] += 1
            if li_c[li[j][i]-1] > 1:
                cnt += 1
                break
        if cnt > 0: break

    for k in range(9):            # 3x3 비교
        li_a = [0] * 9
        m = 0
        n = 0
        if m % 3 == 0 and m != 0:
            m = 0
            n += 1
        for i in range(3):
            for j in range(3):
                li_a[li[i+n][j+m]-1] += 1
                if li_a[li[i+n][j+m]-1] > 1:
                    cnt += 1
                    break
        if cnt > 0: break

        m += 3
    result = 1
    if cnt > 0:
        result = 0
    print(f'#{TC} {result}')


