import sys

input = sys.stdin.readline

def YESorNo():
    n = int(input())
    phone_num = {input().rstrip() for i in range(n)}
    for num in phone_num:
        for j in range(1, len(num)):
            if num[0:j] in phone_num:
                return False
    return True


t = int(input())

for TC in range(1, t+1):
    result = YESorNo()
    if result:
        print('YES')
    else:
        print('NO')