import sys
sys.stdin = open("input_2.txt", "r")


def play(s):

    if s == '+':
        p1 = result.pop()
        p2 = result.pop()
        result.append(int(p1) + int(p2))
        return 0
    elif s == '-':
        p1 = result.pop()
        p2 = result.pop()
        result.append(int(p2) - int(p1))
        return 0
    elif s == '/':
        p1 = result.pop()
        p2 = result.pop()
        result.append(int(p2) // int(p1))
        return 0
    elif s == '*':
        p1 = result.pop()
        p2 = result.pop()
        result.append(int(p1) * int(p2))
        return 0
    elif s == '.':
        return

T = int(input())

for TC in range(1, T+1):

    li = list(map(str, input().split()))
    tc_len = len(li)

    stack = []
    result = []
    print('#%d' % TC, end=" ")
    try:
        for i in range(tc_len):
            if li[i] == '+' or li[i] == '*' or li[i] == '/' or li[i] == '-' or li[i] == '.':
                play(li[i])
            else:
                result.append(int(li[i]))
        if len(stack) != 0 or len(result) != 1:
            print('error')
        else:
            print(result[0])
    except:
        print("error")