import sys
sys.stdin = open("input.txt", 'r')

def change(i, j):
    global r
    c_li = [0] * 4
    for k in range(4):
        c_li[k] = li_2[i][j+k]
    for k in range(4):
        c_li[k] = c_li[k] / min(c_li)
    if len(stack) % 8 != 0:
        if c_li[0] == 3 and c_li[1] == 2 and c_li[2] == 1 and c_li[3] == 1:
            stack.append('0')
        elif c_li[0] == 2 and c_li[1] == 2 and c_li[2] == 2 and c_li[3] == 1:
            stack.append('1')
        elif c_li[0] == 2 and c_li[1] == 1 and c_li[2] == 2 and c_li[3] == 2:
            stack.append('2')
        elif c_li[0] == 1 and c_li[1] == 4 and c_li[2] == 1 and c_li[3] == 1:
            stack.append('3')
        elif c_li[0] == 1 and c_li[1] == 1 and c_li[2] == 3 and c_li[3] == 2:
            stack.append('4')
        elif c_li[0] == 1 and c_li[1] == 2 and c_li[2] == 3 and c_li[3] == 1:
            stack.append('5')
        elif c_li[0] == 1 and c_li[1] == 1 and c_li[2] == 1 and c_li[3] == 4:
            stack.append('6')
        elif c_li[0] == 1 and c_li[1] == 3 and c_li[2] == 1 and c_li[3] == 2:
            stack.append('7')
        elif c_li[0] == 1 and c_li[1] == 2 and c_li[2] == 1 and c_li[3] == 3:
            stack.append('8')
        elif c_li[0] == 3 and c_li[1] == 1 and c_li[2] == 1 and c_li[3] == 2:
            stack.append('9')
        else:
            r = 'F'
    else:
        if c_li[0] >= 3 and c_li[1] == 2 and c_li[2] == 1 and c_li[3] == 1:
            stack.append('0')
        elif c_li[0] >= 2 and c_li[1] == 2 and c_li[2] == 2 and c_li[3] == 1:
            stack.append('1')
        elif c_li[0] >= 2 and c_li[1] == 1 and c_li[2] == 2 and c_li[3] == 2:
            stack.append('2')
        elif c_li[0] >= 1 and c_li[1] == 4 and c_li[2] == 1 and c_li[3] == 1:
            stack.append('3')
        elif c_li[0] >= 1 and c_li[1] == 1 and c_li[2] == 3 and c_li[3] == 2:
            stack.append('4')
        elif c_li[0] >= 1 and c_li[1] == 2 and c_li[2] == 3 and c_li[3] == 1:
            stack.append('5')
        elif c_li[0] >= 1 and c_li[1] == 1 and c_li[2] == 1 and c_li[3] == 4:
            stack.append('6')
        elif c_li[0] >= 1 and c_li[1] == 3 and c_li[2] == 1 and c_li[3] == 2:
            stack.append('7')
        elif c_li[0] >= 1 and c_li[1] == 2 and c_li[2] == 1 and c_li[3] == 3:
            stack.append('8')
        elif c_li[0] >= 3 and c_li[1] == 1 and c_li[2] == 1 and c_li[3] == 2:
            stack.append('9')
        else:
            r = 'F'



def play(n):
    if ord(n) >= 65:
        n = ord(n)-55
        return play2(n)
    else:
        n = int(n)
        return play2(n)



def play2(num):
    stack = []
    for i in range(4):
        stack.append(num % 2)
        num = num // 2

    return stack

T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    li = []
    b = False
    r_i = 0
    for _ in range(N):
        li.append(list(input()))
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            a = li[i].pop(j)
            li_ = play(a)
            for k in li_:
                li[i].insert(j,k)

    li_2 = []
    li_2_len = []
    for i in range(len(li)):
        li_3=[]
        cnt = 1
        for j in range(len(li[i])-1):
            if j == len(li[i])-1:
                li_3.append(cnt)
                break
            if li[i][j] == li[i][j+1]:
                cnt += 1
                continue
            else:
                li_3.append(cnt)
                cnt = 1
        if li_3 not in li_2 and li_3:
            li_2.append(li_3)

    for i in range(len(li_2)):
        li_2_len.append(len(li_2[i]))

    result_sum = []
    for i in range(len(li_2)):
        stack = []
        v = []
        j = 0
        while j < len(li_2[i])-3:
            if j % 2 != 0:
                j += 1
                continue
            r = 'T'
            change(i, j)
            if r == 'T':
                j += 4
            else:
                j += 1
        stack = list(map(int, stack))
        result = 0
        if len(stack) == 8:
            result = (stack[0] + stack[2] + stack[4] + stack[6]) * 3 + stack[1] + stack[3] + stack[5] + stack[7]
        if result % 10 == 0 and result != 0:
            result_sum.append(sum(stack))
    if result_sum:
        print('#%d %d' % (TC, sum(result_sum)))
    else:
        print('#%d %d' % (TC, 0))
