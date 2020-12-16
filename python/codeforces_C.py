T = int(input())

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

li_check = [0] * 9
result = []
for i in range(1, 2 ** 9 + 1):
    stack = []
    for j in range(9):
        if i & (1 << j):
            stack.append(j+1)
    t = stack[:]
    result.append(t)

for TC in range(1, T + 1):
    n = int(input())
    sol = []
    for i in range(len(result)):
        if sum(result[i]) == n:
            total = 0
            for k in range(len(result[i])):
                total += result[i][k] * (10**(len(result[i])-k-1))
            sol.append(total)
    if sol:
        print(min(sol))
    else:
        print(-1)


