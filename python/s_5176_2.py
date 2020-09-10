import sys
sys.stdin = open("input_5177.txt", "r")


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    tree = [0]
    li = list(map(int, input().split()))
    for i in li:
        num = len(tree)
        tree.append(i)
        while num >= 2:
            if li[num] < li[num // 2]:
                li[num], li[num // 2] = li[num // 2], li[num]
                num = num // 2
        else:
            pass


    print(tree)
