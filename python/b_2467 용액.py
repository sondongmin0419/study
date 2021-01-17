N = int(input())

arr = list(map(int, input().split()))

result = abs(arr[0] + arr[-1])
a, b = arr[0], arr[-1]
end = N - 1

if arr[-1] < 0:
    print(arr[-2], arr[-1])
elif arr[0] > 0:
    print(arr[0], arr[1])
else:
    for i in range(N):
        if i >= end:
            break
        if arr[i] > 0 and i < N - 1:
            val = arr[i] + arr[i + 1]
            if val < result:
                result = val
                a, b = arr[i], arr[i + 1]
                break
        before_val = abs(arr[i] + arr[end])
        if before_val < result:
            result = before_val
            a, b = arr[i], arr[end]
        for j in range(end, i, -1):
            val = abs(arr[i] + arr[j])
            if val > before_val:
                end = j+1
                break
            if val < result:
                result = val
                a = arr[i]
                b = arr[j]
                end = j
            before_val = val

    print(a, b)
