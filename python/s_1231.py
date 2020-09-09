import sys
sys.stdin = open("input_1.txt", "r")


def play():
    n = 1
    result = ""
    while True:
        if len(li[n-1]) == 2:
            result += li[n-1][1]
        elif len(li[n-1]) == 3:
            stack.append(n)
            stack.append(li[n-1].pop())
        elif len(li[n-1]) == 4:
            stack.append(li[n-1].pop())
            stack.append(n)
            stack.append(li[n-1].pop())
        if stack:
            n = int(stack.pop())
        else:
            return result


T = 10

for TC in range(1, T+1):
    N = int(input())
    stack = []
    li = [list(map(str, input().split())) for _ in range(N)]
    result_s = play()
    print('#%d %s'% (TC,result_s))


