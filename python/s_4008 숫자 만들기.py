def play(n):
    if n == N-1:
        t_s = li_n[:]
        for i in range(len(stack)):
            t_s.insert(0, cal(stack[i], t_s.pop(0), t_s.pop(0)))
        sum_n.append(t_s[0])
    for i in range(4):
        if visited[i] < li_s[i]:
            visited[i] += 1
            stack.append(i)
            play(n+1)
            visited[i] -= 1
            stack.pop()


def cal(s, a, b):
    if s == 0:
        return a+b
    elif s == 1:
        return a-b
    elif s == 2:
        return a*b
    elif s == 3:
        if a/b < 0:
            return -int(abs(a/b))
        else:
            return a//b

T = int(input())

for TC in range(1, T+1):

    N = int(input())
    li_s = list(map(int, input().split()))  # + - * /
    li_n = list(map(int, input().split()))
    visited = [0, 0, 0, 0]
    stack = []
    sum_n = []
    play(0)
    print('#%d %s' %(TC, max(sum_n) - min(sum_n)))
