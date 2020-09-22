li_c = []
li_s = []


def check(i, j):
    for i_c in range(5):
        for j_c in range(5):
            if li_s[i][j] == li_c[i_c][j_c]:
                li_c[i_c][j_c] = 0
                return


def bingo():
    sum_x = 0
    sum_rx = 0
    b_cnt = 0

    for i in range(5):
        sum_r = 0
        sum_c = 0
        for j in range(5):
            sum_r += li_c[i][j]
            sum_c += li_c[j][i]
            if i == j:
                sum_x += li_c[i][j]
            if i+j == 4:
                sum_rx += li_c[i][j]
        if sum_r == 0:
            b_cnt += 1
        if sum_c == 0:
            b_cnt += 1
    if sum_x == 0:
        b_cnt += 1
    if sum_rx == 0:
        b_cnt += 1

    return b_cnt


for i in range(5):
    li_c.append(list(map(int, input().split())))

for i in range(5):
    li_s.append(list(map(int, input().split())))

cnt = 0
result = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        check(i, j)
        result = bingo()
        if result >= 3:
            break
    if result >= 3:
        break

print(cnt)