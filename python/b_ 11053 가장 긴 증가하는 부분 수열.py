import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
result = [arr[0]]
for i in range(1, N):
    if result[-1] < arr[i]:
        result.append(arr[i])
    else:
        for j in range(len(result)):
            if result[j] >= arr[i]:
                result[j] = arr[i]
                break

print(len(result))