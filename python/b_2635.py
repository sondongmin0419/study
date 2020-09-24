N = int(input())


def play(n1, n2):
    global cnt_max
    global max_stack

    if n1 - n2 >= 0:
        stack.append(n1-n2)
        return play(n2, n1 - n2)
    else:
        if len(stack) > cnt_max:
            cnt_max = len(stack)
            max_stack = stack[::]
        return

cnt_max = 0
max_stack = []
for i in range(1,N+1):
    stack = []
    stack.append(N)
    stack.append(i)
    play(N, i)

print(cnt_max)
print(*max_stack)