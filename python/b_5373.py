def play(test):
    area = test[0]
    r = test[1]
    li_li = []
    if area == 'U':
        li_li.append([0, 1, 2, 3, 4, 5])
    elif area == 'L':
        li_li.append([3, 5, ])
    pass


T = int(input())
li_ = []
li_.append([['w', 'w', 'w'] for _ in range(3)])  # 위 0
li_.append([['g', 'g', 'g'] for _ in range(3)])  # 왼 1
li_.append([['r', 'r', 'r'] for _ in range(3)])  # 앞 2
li_.append([['o', 'o', 'o'] for _ in range(3)])  # 뒤 3
li_.append([['b', 'b', 'b'] for _ in range(3)])  # 오 4
li_.append([['y', 'y', 'y'] for _ in range(3)])  # 아래 5


for TC in range(1, T+1):

    n = int(input())

    li = list(map(str, input().split()))
    for i in range(n):
        play(li[i])
    print(li_)