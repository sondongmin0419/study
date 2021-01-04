import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_n = arr[0]
for i in range(1,n):
    if arr[i-1] >=0:
        arr[i] += arr[i-1]
print(max(arr))
