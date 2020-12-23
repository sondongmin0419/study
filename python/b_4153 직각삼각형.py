import sys

input = sys.stdin.readline

while True:
    li = list(map(int, input().rstrip().split()))
    if sum(li) == 0:
        break
    li.sort()

    if li[2] ** 2 == li[0] ** 2 + li[1] ** 2:
        print('right')
    else:
        print('wrong')
