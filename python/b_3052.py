li = [0] * 10
li_n = [0] * 10

for i in range(10):
    li[i] = int(input())
    li_n[i] = li[i] % 42

li_set = set(li_n)

print(len(li_set))