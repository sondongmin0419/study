n = int(input())
#
# 0000 0000 /  0000 0000 / 0000 0000 / 0000 0000


def d_index():
    for i in range(4):
        for j in range(n):
            if li_li[0][i] != li_li[j][i]:
                return i
    return 4


def d_binary_index():
    for i in range(8):
        for j in range(n):
            if li_binary[0][i] != li_binary[j][i]:
                return i
    return 8


def play(n):
    stack = []
    while True:
        na = n % 2
        stack.append(na)
        n = n // 2
        if n == 1:
            stack.append(1)
            break
        elif n == 0:
            stack.append(0)
            break

    stack_reverse = stack[::-1]
    while len(stack_reverse) < 8:
        stack_reverse.insert(0, 0)
    li_binary.append(stack_reverse)



li_li = [0] * n
s = ''
for i in range(n):
    s = input()
    li = s.split(".")
    li_li[i] = li

d_ind = d_index()
li_binary = []

for i in range(n):
    result = []
    if d_ind == 4:
        d_ind -= 1
    s = li_li[i][d_ind]
    play(int(s))



d_binary_ind = d_binary_index()

f_f_result = []
f_f_mask_result = []
for i in range(4):
    f_stack = []
    f_mask_stack = []
    if i < d_ind:
        f_f_mask_result.append(255)
        f_f_result.append(int(li_li[0][i]))
        continue
    elif i > d_ind:
        f_stack.append(0)
        f_mask_stack.append(0)
        continue
    for j in range(8):
        if j < d_binary_ind:
            f_stack.append(li_binary[0][j])
            f_mask_stack.append(1)
        else:
            f_stack.append(0)
            f_mask_stack.append(0)
    f_f_mask_result.append(f_mask_stack)
    f_f_result.append(f_stack)


def integer_(b_li):
    total = 0
    number = 1
    for i in range(7,-1,-1):
        if b_li[i] == 1:
            total += b_li[i] * number
        number *= 2
    return total

# 주소
for i in range(4):
    if f_f_result[i] != int(li_li[0][i]):
        f_f_result[i] = integer_(f_f_result[i])
        i += 1
        while i < 4:
            f_f_result.append(0)
            i += 1
        if i >= 4:
            break


for i in range(4):
    if f_f_mask_result[i] != 255:
        f_f_mask_result[i] = integer_(f_f_mask_result[i])
        i += 1
        while i < 4:
            f_f_mask_result.append(0)
            i += 1
        if i >= 4:
            break

# if n != 1:
for i in range(4):
    print(f_f_result[i], end='')
    if i != 3:
        print('.', end='')
print()
for i in range(4):
    print(f_f_mask_result[i], end='')
    if i != 3:
        print('.', end='')
