num = int(input())
li = [[0] * 101 for _ in range(101)]
for i in range(num):
    a, b = map(int, input().split())

    for r in range(a, a+10):
        for c in range(b, b+10):
            li[r][c] = 1
area = 0
for i in range(101):
    for j in range(101):
        if li[i][j] == 1:
            area += 1

print(area)