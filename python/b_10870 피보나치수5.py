n = int(input())

li = [0 for _ in range(n + 2)]
li[1] = 1

for i in range(2, n + 1):
    li[i] = li[i - 1] + li[i - 2]
print(li[n])
