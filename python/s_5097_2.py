T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    print('#%d %d' % (TC, li[M % N]))
