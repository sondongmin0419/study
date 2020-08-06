li = [0] * 9

max_li = 0
max_index = 0
for i in range(9):
    li[i] = int(input())
    if li[i] > max_li:
        max_li = li[i]
        max_index = i+1

print(max_li)
print(max_index)