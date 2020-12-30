N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

max_sum = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            s= arr[i] + arr[j] + arr[k]
            if s > max_sum and s <= M:
                max_sum = s
print(max_sum)