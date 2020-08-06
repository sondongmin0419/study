n = int(input())

li_score = list(map(int, input().split()))
max_score = max(li_score)
total = 0
for i in range(n):
    total += (li_score[i]/max_score)*100

print(total/n)