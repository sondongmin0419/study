import sys
sys.stdin = open("input_1.txt", "r")

T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())

    li = list(map(int, input().split()))

    for i in range(M):
        s = li.pop(0)
        li.append(s)

    print('#%d %d' % (TC, li[0]))