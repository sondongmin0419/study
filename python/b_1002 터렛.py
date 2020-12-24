import sys

input = sys.stdin.readline

n = int(input())

for TC in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif r1 + r2 == distance or distance+min(r1,r2) == max(r1,r2):
        print(1)
    elif r1 + r2 < distance or distance+min(r1,r2) < max(r1,r2):
        print(0)
    else:
        print(2)

