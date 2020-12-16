from collections import deque

T = int(input())

for TC in range(1, T + 1):
    n = int(input())
    d = deque(map(int, input().split()))
    i = 0
    while i < n:
        print(d.popleft(), end=' ')
        i += 1
        if i < n:
            print(d.pop(), end=' ')
            i += 1
    print()
