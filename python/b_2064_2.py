n = int(input())


def check():
    for i in range(4):
        test = li_li[0][i]
        for j in range(n):
            if test != li_li[j][i]:
                return i
    return 5


def check_2(c_c):
    for i in range(7,-1,-1):
        test = int(li_li[0][c_c]) & 1<<i
        for j in range(n):
            if int(li_li[j][c_c]) & 1 << i != test:
                return i
    return 8


def make_result_i():
    global result_i
    for i in range(4):
        if i == c:
            result_ii = 0
            for j in range(7, -1, -1):
                if j != c2:
                    result_ii += 2 **j & int(li_li[0][i])
                else:
                    result_i += str(result_ii)
                    return
            result_i += str(result_ii)
        else:
            result_i += str(li_li[0][i])
        if i != 3:
            result_i += '.'


def make_result_m():
    global result_m
    for i in range(4):
        if i == c:
            result_ii = 0
            for j in range(7, -1, -1):
                if j != c2:
                    result_ii += 2 ** j
                else:
                    result_m += str(result_ii)
                    return
            result_m += str(result_ii)
        else:
            result_m += '255'
        if i != 3:
            result_m += '.'


li_li = [0] * n
s = ''
for i in range(n):
    s = input()
    li = s.split(".")
    li_li[i] = li


c = check()
if c == 5:
    pass
else:
    c2 = check_2(c)

result_i = ''
result_m = ''

make_result_i()
make_result_m()
while result_i.count('.') < 3:
    result_i += '.0'
while result_m.count('.') < 3:
    result_m += '.0'

print(result_i)
print(result_m)