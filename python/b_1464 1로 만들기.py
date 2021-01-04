N = int(input())

arr = [N for _ in range(N+1)]

arr[N] = 0
for i in range(N,0,-1):
    if arr[i] == N:
        continue
    else:
        if i % 3 == 0:
            arr[i//3] = min(arr[i//3], arr[i]+1)
        if i % 2 == 0:
            arr[i//2] = min(arr[i//2], arr[i]+1)
        arr[i-1] = min(arr[i-1], arr[i]+1)

print(arr[1])