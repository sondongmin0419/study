N = int(input())

li = []
li_s = [[] for _ in range(N)]
for i in range(N):
    li.append(list(map(int, input().split())))
    li_s[i].append((li[i][0], li[i][5]))
    li_s[i].append((li[i][1], li[i][3]))
    li_s[i].append((li[i][2], li[i][4]))
max_sum = 0

for n in range(1,7):
    sum_n = 0
    max_n = 0
    t_n = 0
    a = b = 0
    for k in range(3):
        if n in li_s[0][k]:
            a,b = li_s[0][k]
        else:
            nnn = max(li_s[0][k])
            if max_n < nnn:
                max_n = nnn
    if a == n:
        t_n = b
    else:
        t_n = a
    sum_n += max_n
    for i in range(1,N):
        max_n = 0
        for kk in range(3):
            if t_n in li_s[i][kk]:
                a, b = li_s[i][kk]
            else:
                nnn = max(li_s[i][kk])
                if max_n < nnn:
                    max_n = nnn
        if a == t_n:
            t_n = b
        else:
            t_n = a
        sum_n += max_n
    if sum_n > max_sum:
        max_sum = sum_n
print(max_sum)
