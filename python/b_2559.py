N, K = map(int, input().split())

li = list(map(int, input().split()))

max_sum = sum(li[0:K])
sum = max_sum
for i in range(K,N):
    sum = sum + li[i] - li[i-K]
    if sum > max_sum:
        max_sum = sum

print(max_sum)