N, M = map(int, input().split())

a = N
b = N // 2
c = N - b
d = (N - 1) // 3 + 1

arr = [a, b, c, d]
button = [0 for _ in range(N + 1)]
result_set = set()
stack = []
b_stack = [0] * 4
button_copy = button[:]
for i in range(2 ** 4 - 1):
    stack = []
    total = 0
    for k in range(4):
        if i & 1 << k:
            stack.append(1)
            total += arr[k]
        else:
            stack.append(0)
    if total <= M:
        if stack[0] != b_stack[0]:
            for c in range(1, len(button)):
                button_copy[c] = (button_copy[c] + 1) % 2
        if stack[1] != b_stack[1]:
            for c in range(2, len(button), 2):
                button_copy[c] = (button_copy[c] + 1) % 2
        if stack[2] != b_stack[2]:
            for c in range(1, len(button), 2):
                button_copy[c] = (button_copy[c] + 1) % 2
        if stack[3] != b_stack[3]:
            for c in range(1, len(button), 3):
                button_copy[c] = (button_copy[c] + 1) % 2
        result_set.add(str(button_copy)[1::3])
        b_stack = stack[:]

print(len(result_set))
