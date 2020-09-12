N = int(input())
K = int(input())

def play(y, x):
    na = y % 3  # 1 빨강, 2 파랑, 0 노랑
    m = x % 3  #
    if y <= x <= N+1 - y:
        if na == 1:
            return 1 # 빨강
        elif na == 2:
            return 2 # 파랑
        else:
            return 3 # 노랑
    else:
        if m == 1:
            return 1 # 빨강
        elif m == 2:
            return 2 # 파랑
        else:
            return 3 # 노랑


for i in range(K):
    x, y = map(int, input().split())
    if x + y > N+1:
        x2 = - y + N+1
        k = x - x2
        y = y - k
        x = x2
    print(y, x)
    print(play(y, x))