import sys

input = sys.stdin.readline

def YESorNo():
    n = int(input())
    numbers = {}
    last_w = 0
    for i in range(n):
        num = input().rstrip()
        current_dict = numbers
        for w in num:
            if last_w in current_dict:
                return False
            current_dict = current_dict.setdefault(w, {})
        current_dict[last_w] = last_w
    return True

t = int(input())

for TC in range(1, t+1):
    result = YESorNo()
    if result:
        print('YES')
    else:
        print('NO')