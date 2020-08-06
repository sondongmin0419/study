import sys

n = int(input())

li = [0] * n

for i in range(n):
    li[i] = input()
    cnt = 0
    total = 0
    for j in li[i]:
        if j == 'O':
            cnt += 1
            total += cnt
        else:
            cnt =0
    print(total)



