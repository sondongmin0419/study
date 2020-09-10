import sys
sys.stdin = open("input_1232.txt", "r")


def maketree(n):
    len_li = len(li[n-1])
    if len_li == 2:
        return int(li[n-1][1])
    else:
        num1 = int(li[n-1].pop())
        num2 = int(li[n-1].pop())
        if li[n-1][1] == '+':
            return maketree(num2) + maketree(num1)
        elif li[n-1][1] == '-':
            return maketree(num2) - maketree(num1)
        elif li[n-1][1] == '*':
            return maketree(num2) * maketree(num1)
        elif li[n-1][1] == '/':
            return maketree(num2) / maketree(num1)



T = 10

for TC in range(1, T+1):
    N = int(input())

    li = [list(map(str, input().split())) for _ in range(N)]

    tree = [0] * (N+1)

    result = maketree(1)

    print('#%d %d' % (TC, result))
