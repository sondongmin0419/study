import sys
import math

T = int(input())

for TC in range(1, T + 1):
    check = False
    n = int(input())

    li = list(map(int, input().split()))
    S = sum(li)
    e = S / (2*n)
    e_ = S/ n
    result_e = e_+(e_-e)//2
    result = list(int(result_e) for _ in range(n))
    p = 0n
    for i in range(n):
        p += abs(li[i]-result[i])
    if p *2 < S:
        print(result)
    else:
        print(result)
