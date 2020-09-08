import sys
sys.stdin = open("input_4.txt", "r")


def play(t):
    if li_check[test] == 0 and li_li[test] and li_li[test]!=0:
        for j in li_li[test]:
            if li_v[t][j] == 1:
                li_check[j] -= 1
                stack.append(j)


T = 10

for TC in range(1, T+1):
    stack = []
    stack_2 = []
    V, E = map(int, input().split())
    visited = [0] * (V+1)

    li_e = list(map(int, input().split()))
    li_v = [[0] * (V+1) for _ in range(V+1)]
    li_check = [0]*(V+1)
    li_li = [0] * (V+1)
    for i in range(len(li_e)//2):
        li_v[li_e[i*2]][li_e[i*2+1]] = 1
        li_check[li_e[i*2+1]] += 1
        if li_li[li_e[i*2]] == 0:
            li_li[li_e[i * 2]] = [li_e[i*2+1]]
        else:
            li_li[li_e[i*2]].append(li_e[i*2+1])

    for i in range(1, V+1):
        if li_check[i] == 0:
            if i not in stack:
                stack.append(i)
    while True:
        test = stack.pop(0)
        while True:
            if visited[test] == 1:
                test = stack.pop(0)
                continue
            if li_check[test] == 0:
                break
            else:
                if test not in stack:
                    stack.append(test)
                test = stack.pop(0)
        stack_2.append(test)
        visited[test] = 1
        play(test)
        if len(stack_2) == V:
            break


    print('#%d' % TC,end=" ")
    print(*stack_2)


