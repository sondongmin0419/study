import math
import sys
# input = sys.stdin.readline

X, Y = map(int, input().split())

before_Z = Y * 100 // X

if before_Z >= 99:
    print(-1)
else:
    after_Z = before_Z + 1

    d_X = (after_Z * X - 100 * Y) / (100 - after_Z)

    print(math.ceil(d_X))
