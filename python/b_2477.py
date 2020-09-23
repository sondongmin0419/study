K = int(input())

li_count = [0] * 6
li_1 = []
li_2 = []
for i in range(6):
    a, b = map(int, input().split())
    if li_count[a] == 0:
        li_count[a] += 1
        li_1.append([a,b])
    else:
        li_2.append([a,b])

area_1 = max(li_1[0][1], li_1[2][1]) * max(li_1[1][1], li_1[3][1])
if li_2[0][0] == li_1[0][0]:
    li_2[0][1] *= -1
area_2 = li_2[0][1] * li_2[1][1]
print(area_1)
print(area_2)
print(area_1 + area_2)