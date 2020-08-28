def check(s, co, stack):

    for j in range(N):
        if li[s][j] != 0 and j not in stack:
            stack.append(j)
            co += li[s][j]
            if len(stack) == N or co > cost_t[0]:
                if li[j][stack[0]] != 0 and len(stack) == N:
                    co += li[j][stack[0]]
                    if cost_t[0] > co:
                        cost_t[0] = co
                    print(stack)
                stack.pop()
                co -= li[s][j]

                return
            else:
                check(j, co, stack)
                co -= li[s][j]
                stack.pop()


N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    stack = []
    cost_t = [1000000*11]
    cost = 0
    stack.append(i)
    check(i, cost, stack)
print(cost_t[0])