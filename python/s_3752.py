import sys
sys.stdin = open("input_2.txt", "r")

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    li_li = []
    li_set = set(li)
    for i in range(len(li_set)):
        test = li_set.pop()
        li_li.append([test, li.count(test)])

    total = 1
    print(li_li)
    for i in range(len(li_li)):
        total *= (li_li[i][1]+1)
    print(total)