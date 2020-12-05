T = int(input())

def play(n):
    if len(stack) == N//2:
        s_ = stack[:]
        A.append(s_)
        return
    for i in range(n,N):
        if i not in stack:
            stack.append(i)
            play(i+1)
            stack.pop()
    return


def play2():


    return

for TC in range(1, T + 1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]

    A = []
    stack = []
    result = 20000*N
    play(0)

    while A:
        sum_A = 0
        sum_B = 0
        food_a = A.pop()
        food_b = []
        for i in range(N):
            if i not in food_a:
                food_b.append(i)
        for i in range(N//2-1):
            for j in range(i+1,N//2):
                if i != j:
                    sum_A += (li[food_a[i]][food_a[j]] + li[food_a[j]][food_a[i]])
                    sum_B += (li[food_b[i]][food_b[j]] + li[food_b[j]][food_b[i]])
        if abs(sum_A-sum_B) < result:
            result = abs(sum_A-sum_B)



    print('#%d %d' %(TC, result))

