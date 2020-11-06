def play(n):
    for i in range(n, 10):
        if li[i] not in stack:
            stack.append(li[i])
            sum_stack = sum(stack)

            if sum_stack == 10:
                s_li = stack[:]
                s_li.sort()
                if s_li not in result:
                    result.append(s_li)
                stack.pop()
                return

            elif sum_stack > 10:
                stack.pop()
                return

            play(n+1)
            stack.pop()


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li_c = [0] * 10

n = 0
result = []
stack = []

play(0)
print(result)