T = int(input())

li = [0] * T
li_lank = [1] * T
for i in range(T):
    li[i] = list(map(int, input().split()))

for i in range(T):
    for j in range(T):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            li_lank[i] += 1
for i in range(T):
    print(f'{li_lank[i]}', end=' ')
