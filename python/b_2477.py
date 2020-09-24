K = int(input())

li_1 = []
max_w = 0
max_h = 0
w_i = 0
h_i = 0
for i in range(6):
    a, b = map(int, input().split())
    li_1.append([a,b])
    if a == 1 or a == 2:
        if b > max_w:
            max_w = b
            w_i = i
    else:
        if b > max_h:
            max_h = b
            h_i = i
area_1 = max_h * max_w
area_2 = li_1[(w_i+3) % 6][1] * li_1[(h_i+3) % 6][1]
result = area_1 - area_2
print(result * K)