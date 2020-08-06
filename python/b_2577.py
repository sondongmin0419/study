li = [0]*3

num = 1

for i in range(3):
    li[i] = int(input())
    num *= li[i]

st_num = str(num)
li_2 = [0] * len(st_num)
li_index = 0
for i in st_num:
    li_2[li_index] = i
    li_index += 1 
for i in range(0,10):
    cnt = li_2.count(str(i))
    print(cnt)

