import sys
sys.stdin = open("input_3.txt", "r")

def check():
    global result
    while True:
        if len(s) > 0:
            s_test = s.pop()
            if s_test == 'S' or s_test == 'D' or s_test == 'H' or s_test == 'C':
                if s_test == 'D':
                    s_test_n = stack.pop()
                    if s_test_n in li_D:
                        result = 1
                        return
                    else:
                        li_D.append(s_test_n)
                elif s_test == 'S':
                    s_test_n = stack.pop()
                    if s_test_n in li_S:
                        result = 1
                        return
                    else:
                        li_S.append(s_test_n)
                elif s_test == 'C':
                    s_test_n = stack.pop()
                    if s_test_n in li_C:
                        result = 1
                        return
                    else:
                        li_C.append(s_test_n)
                elif s_test == 'H':
                    s_test_n = stack.pop()
                    if s_test_n in li_H:
                        result = 1
                        return
                    else:
                        li_H.append(s_test_n)
            else:
                s_test_2 = s.pop()
                s_test_n = s_test_2 + s_test

                stack.append(s_test_n)
        else:
            return


T = int(input())

for TC in range(1, T+1):
    s = list(input())
    result = 0
    stack = []
    li_S = []
    li_D = []
    li_H = []
    li_C = []
    check()
    print(li_S, li_D, li_H, li_C)
    if result == 1:
        print('#%d ERROR' % TC)
    else:
        print('#%d %d %d %d %d' % (TC, 13-len(li_S), 13-len(li_D), 13-len(li_H), 13-len(li_C)))
