li = [0] * 9
li_i = [0] * 9

for i in range(9):
    li[i] = int(input())
li.sort()
# 12 13 14 15 16 17 18 19
# 23 24 25 26 27 28 29
result = 0
for i in range(9):
    li_i[i] = 1
    for j in range(i+1,9):
        li_i[j] = 1
        sum_i = 0
        for k in range(9):
            if k != i and k != j:
                sum_i += li[k]
        if sum_i == 100:
            result = 1
            break
        li_i[j] = 0
    if result == 1:
        break
    li_i[i] = 0
li_r = []
for i in range(9):
    if li_i[i] == 0:
        print(li[i])
