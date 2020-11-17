N = int(input())

li = list(map(int, input().split()))
li_2 = [[0, 0] for _ in range(N+1)]

for i in range(N):
    li_2[i] = [i+1, li[i]]

li_2.sort(key=lambda x: x[1]+ x[0])

s = 0
e = 0
cnt = 0
print(li_2)
for i in range(1, N+1):
    
    if li_2[i][0] >= s and li_2[i][1] >= e:
        cnt += 1
        s = li_2[i][0]
        e = li_2[i][1]
        print(s, e)
print(N-cnt)