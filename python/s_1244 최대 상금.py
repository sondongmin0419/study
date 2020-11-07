def play(test_li):
    for i in range(len(test_li)-1):
        for j in range(i+1, len(test_li)):
            if i != j:
                new_li = test_li[:]
                new_li[i], new_li[j] = new_li[j], new_li[i]
                b_li.append(''.join(new_li))


T = int(input())

for TC in range(1, T+1):
    bonus, n = map(int, input().split())

    b_set = set()
    b_li = [str(bonus)]
    for _ in range(n):
        b_li = list(set(b_li))

        for __ in range(len(b_li)):

            play(list(b_li.pop(0)))
    b_li.sort(reverse=True)
    print('#%d %d' %(TC, int(b_li[0])))

