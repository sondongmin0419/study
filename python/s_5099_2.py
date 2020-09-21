T = int(input())


def play():
    while True:
        while len(li_in) < N and li_li_pizza:
            li_in.append(li_li_pizza.pop(0))
        for i in range(len(li_in)):
            pizza = li_in.pop(0)
            pizza[0] = pizza[0] // 2

            if pizza[0] != 0:
                li_in.append(pizza)
            elif len(li_in) == 1:
                return
            else:
                break


for TC in range(1, T+1):
    N, M = map(int, input().split())
    li_pizza = list(map(int, input().split()))
    li_li_pizza = [0] * M
    for i in range(M):
        li_li_pizza[i] = [li_pizza[i], i+1]
    li_in = []
    result = []
    play()
    print('#%d %d' % (TC,li_in[0][1]))