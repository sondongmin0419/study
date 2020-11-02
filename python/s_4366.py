def play2(n):
    sum = 0
    for i in range(len(li_2)-1, -1, -1):
        if i != n:
            sum += li_2[i] * 2 ** (len(li_2)-1-i)
        else:
            sum += (li_2[i]+1) % 2 * 2 ** (len(li_2)-1-i)
    li_2_result.append(sum)


def play3(n):
    sum = 0

    for i in range(len(li_3)-1, -1, -1):
        if i != n:
            sum += li_3[i] * 3 ** (len(li_3)-1-i)
        else:
            sum += (li_3[i]+1) % 3 * 3 ** (len(li_3)-1-i)
    li_3_result.append(sum)


def play3_2(n):
    sum = 0

    for i in range(len(li_3) - 1, -1, -1):
        if i != n:
            sum += li_3[i] * 3 ** (len(li_3) - 1 - i)
        else:
            sum += (li_3[i]+2) % 3 * 3 ** (len(li_3) - 1 - i)
    li_3_result.append(sum)


T = int(input())

for TC in range(1, T+1):
    li_2 = list(map(int, list(input())))
    li_3 = list(map(int, list(input())))

    li_2_result = []
    li_3_result = []

    for i in range(len(li_2)):
        play2(i)
    for i in range(len(li_3)):
        play3(i)
        play3_2(i)

    for num in li_2_result:
        if num in li_3_result:
            print('#%d %d' % (TC, num))
            break