import sys
import math

input = sys.stdin.readline

N = int(input())

arr = [0] * 8001
total = 0
for _ in range(N):
    n = int(input())
    arr[n + 4000] += 1
    total += n


print(round(total / N))

cnt = 0
for i in range(8001):
    cnt += arr[i]
    if cnt >= N //2+1:
        print(i - 4000)
        break

max_cnt = max(arr)
max_n = []
for i in range(8001):
    if arr[i] == max_cnt:
        max_n.append(i)
if len(max_n) > 1:
    print(max_n[1] - 4000)
else:
    print(max_n[0] - 4000)

h = 0
l = 0
for i in range(8001):
    if arr[i] != 0:
        l = i
        break
for j in range(8000, 0, -1):
    if arr[j] != 0:
        h = j
        break
print(h - l)
