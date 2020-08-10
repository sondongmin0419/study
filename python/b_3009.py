list_x = []
list_y = []

for i in range(3):
    a, b = map(int, input().split())
    list_x += [a]
    list_y += [b]
for i in range(3):
    if list_x.count(list_x[i]) == 1:
        print(list_x[i], end=' ')
for i in range(3):
    if list_y.count(list_y[i]) == 1:
        print(list_y[i])