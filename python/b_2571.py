N = int(input())

li = [[0] * 100 for _ in range(100)]
li_1 = [[[1,1] for _ in range(100)] for _ in range(100)]
max_area = 0
maxx = 0
maxy = 0
for n in range(N):
    x, y = map(int, input().split())
    for r in range(x,x+10):
        for c in range(y,y+10):
            li[c][r] = 1

for y in range(100):
    for x in range(100):
        if x-1 >= 0:
            if li[y][x-1] == 1:
                li_1[y][x][0] = li_1[y][x-1][0] + 1
            else:
                li_1[y][x][0] = 1
        if y-1 >= 0:
            if li[y-1][x] == 1:
                li_1[y][x][1] = li_1[y-1][x][1] + 1
            else:
                li_1[y][x][1] = 1
        area = li_1[y][x][0] * li_1[y][x][1]
        
        if area > max_area:
            max_area = area
            maxx = x
            maxy = y

print(max_area)