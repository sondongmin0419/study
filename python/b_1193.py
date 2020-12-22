import math

n = int(input())

i = 0
total = 0

k = int(math.sqrt(n * 2))
while k * (k + 1)//2 < n:
    k += 1
p = k * (k + 1)//2 - n
if k % 2 == 0:
    print(str(k - p) + '/' + str(1 + p))
else:
    print(str(1 + p) + "/" + str(k - p))