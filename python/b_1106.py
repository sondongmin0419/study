def price (list_a):
    for i in range(10):
        li[0]*i

C, N = map(int, input().split())

li = []
li_ef = []
for city in range(N):
    mini = list(map(int, input().split()))
    mini.append(mini[1]/mini[0])
    li.append(mini)

for i in range(N-1):
    for j in range(N):
        if li[i][2] < li[j][2]:
            li[i], li[j] = li[j], li[i]

print(money)