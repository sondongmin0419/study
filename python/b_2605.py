s_num = int(input())

li = list(map(int, input().split()))
result_li = []
for i in range(1,s_num+1):
    result_li.insert(len(result_li)-li[i-1], i)

print(*result_li)